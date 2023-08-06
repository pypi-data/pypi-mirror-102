import boto3
from botocore.exceptions import EndpointConnectionError
from datetime import datetime
import pandas as pd
from pathlib import Path
import time
import warnings
from hashlib import md5

MAX_QUERY_STRING_BYTES = 262144
class AthenaQuery():
  def __init__(self, query_string=None, **kwargs):
    
    if kwargs.get("id") is None and query_string is not None:
      self.bytes_usage = len(query_string.encode('utf-8')) / MAX_QUERY_STRING_BYTES

      if self.bytes_usage >= 1:
        raise ValueError("query maximum bytes reached")
      elif self.bytes_usage >= .8:
        warnings.warn("query size almost at maximum percent", self.bytes_usage)
    
    self.query_string = query_string
    self.sql = query_string  # convenience alias
    self.fingerprint = md5(query_string.encode()).hexdigest()

    self.client = kwargs.get("client", boto3.client('athena', region_name="us-east-1"))
    self.s3 = kwargs.get("s3", boto3.client("s3"))

    self.database = kwargs.get("database", "default")
    self.s3_result_folder = kwargs.get("s3_result_folder", "results")
    self.catalog = kwargs.get("catalog", "AwsDataCatalog")
    self.max_results = kwargs.get("max_results", 100)
    self.id = kwargs.get("id", None)
    self.response = None
    self.verbose = kwargs.get("verbose", False)
    self.completed = False
    self.cached_status = "unknown"
    self.cache_seconds = kwargs.get("cache_seconds", 20)
    self.sleep_secs = kwargs.get("sleep_secs", 30)
    self.retried = False
    self.last_status_update_time = datetime(1800, 1, 1)  # way in the past
    self.results_dir = Path(kwargs.get("results_dir", "/tmp"))

  def execute(self):
    res = self.client.start_query_execution(
        QueryString=self.query_string,
        QueryExecutionContext={
            'Database': self.database,
            'Catalog': self.catalog
        }
    )

    self.response = res
    assert res['ResponseMetadata']['HTTPStatusCode'] == 200, res
    self.id = res['QueryExecutionId']
    return self.id
  
  def get_execution_status(self):
    return self.client.get_query_execution(QueryExecutionId=self.id)

  def status(self, cache_seconds=None, force=False):
    """
    Returns status for an AthenaQuery.

    If completed or cache_seconds has not elapsed yet, a cached response will be returned
    """
    if not self.is_executed():
      return "not-executed"

    if not force and self.should_return_cached_status(cache_seconds=cache_seconds):
      return self.cached_status

    res = self.get_execution_status()
    self.response = res

    status = res['QueryExecution']['Status']['State'].lower()
    if status in ["failed", "succeeded", "cancelled"]:
      self.cached_status = status
      self.completed = True

    self.last_status_update_time = datetime.now()
    return status

  def should_return_cached_status(self, cache_seconds=None):
    if cache_seconds is None:
      cache_seconds = self.cache_seconds
    return self.completed or self.seconds_since_last_status_update() < cache_seconds

  def seconds_since_last_status_update(self):
    delta = datetime.now() - self.last_status_update_time
    return delta.seconds

  def is_executed(self):
    return self.id is not None

  def state_change_reason(self):
    return self.response['QueryExecution']['Status']['StateChangeReason']
  
  def results(self, wait=True, max_tries=5000, cache_seconds=None, download=False):
    """
    Pass download=True if you want full results, not just the first page.
    """
    if not self.is_executed():
      return "not-executed"

    if cache_seconds is None:
      cache_seconds = self.cache_seconds

    if wait:
      cache_seconds = 0 # don't cache when waiting on result

    status = self.status(cache_seconds=cache_seconds)

    if not wait and status not in ['succeeded']:
      return status

    if download:
      self.wait(status=status, max_tries=max_tries, cache_seconds=cache_seconds)      
      return pd.read_csv(self.download_results())
    else:
      results = self.client.get_query_results(
          QueryExecutionId=self.id, MaxResults=self.max_results)
      self.response = results
      return to_df(results)

  
  def wait(self, status="unknown", max_tries=5000, cache_seconds=None, sleep_secs=None):    
    sleep_secs = sleep_secs or self.sleep_secs
    attempts = 0
    while status != 'succeeded':
      time.sleep(sleep_secs)
      status = self.status(cache_seconds=cache_seconds)
      if status == 'failed':
        raise ValueError(self.state_change_reason())
      if status == 'cancelled':
        raise ValueError("query was cancelled")
      attempts += 1

      if attempts >= max_tries:
        raise ValueError("max tries reached")   
      
  def download_results(self, results_dir=None):
    if not self.is_executed():
      self.execute()
      self.wait()

    fn = self.id+".csv"
    
    if results_dir is None:
      results_dir = self.results_dir
      
    results_dir = Path(results_dir)
    path = results_dir/fn
    
    if path.exists():
      return path
    
    bucket, key = self.remote_location()

    try:
      self.s3.download_file(bucket, key, str(path))
    except EndpointConnectionError:
      warnings.warn("caught EndpointConnectionError. Retrying in 3 seconds...")
      time.sleep(3)
      self.s3.download_file(bucket, key, str(path))

    return path

  def remote_location(self):
    res = self.get_execution_status()
    remote_path = res['QueryExecution']['ResultConfiguration']['OutputLocation']
    remote_path = remote_path.replace("s3://", "")
    folders = remote_path.split("/")
    bucket = folders[0]
    key = "/".join(folders[1:])
    return bucket, key
  
def to_df(ds):
    if len(ds['ResultSet']['Rows']) == 0:
        return

    data = []
    headers = extract_row(ds, 0)

    for _i in range(1, len(ds['ResultSet']['Rows'])):
        data.append(dict(zip(headers, extract_row(ds, 1))))

    return pd.DataFrame(data)

def extract_row(ds, idx):
    return [d.get('VarCharValue', None) for d in ds['ResultSet']['Rows'][idx]['Data']]
