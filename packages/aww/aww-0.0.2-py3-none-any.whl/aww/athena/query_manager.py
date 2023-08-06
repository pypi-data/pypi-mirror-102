import time
from datetime import datetime
from tqdm.auto import tqdm as tqdm # threadsafe fix
import warnings
from datetime import datetime as dt
import math
from .athena_query import AthenaQuery

class AthenaQueryManager():
  """
  service object that I can pass anywhere that easily and intuitively
  collects and drains concurrent queries?
  """

  def __init__(self, **kwargs):
    self.max_concurrency = kwargs.get("max_concurrency", 450)
    self.pending_queries = []
    self.sleep_secs = kwargs.get("sleep_secs", 10)
    self.last_status_update_time = datetime(1800, 1, 1)  # way in the past
    self.log_path = kwargs.get("log_path", "/tmp/queries.txt")
    self.failures = []
    self.s3 = kwargs["s3"]

  def execute_query(self, qry, wait=False):
    """
    Executes a query and adds to pending list.
    If max concurrency is met, this will sleep until there is an opening.
    If wait=True is passed, results will be returned in form of a DataFrame.
    """
    self.ensure_concurrency_limit()
    qry.execute()
    self.pending_queries.append(qry)

    if wait:
      return qry.results(wait=True, max_tries=10000)

  def execute_query_batch(self, queries, desc="batch", disable_progress=False):
    """Takes an array of AthenaQueries and waits for them to complete"""
    if len(queries) == 0:
      return True

    for q in tqdm(queries, desc=desc, disable=disable_progress):
      self.ensure_concurrency_limit()
      self.execute_query(q)

    batch_pending = queries.copy()

    # init tqdm progress bar
    num_pending = len(batch_pending)
    
    while num_pending > 0:
      time.sleep(self.sleep_secs)
      batch_pending = self.filter_for_pending(batch_pending)
      num_pending = len(batch_pending)
    return True
    
  def retry_failures(self):
    self.execute_query_batch(self.failures, desc="retrying failures")

  def update_pending_queries(self, update_threshold=1, force=False, checkwhen=120):
    """
    Updates pending queries when percentage threshold is met, otherwise cached response will be returned.
    
    If checkwhen seconds has been reached, check anyway.
    
    Default percentage threshold is 100% -> update_threshold=1
    """
    
    num_pending = len(self.pending_queries)
    if num_pending == 0:
      return self.pending_queries
    
    # max_wait = math.log(num_pending)*(num_pending*.2) # .2 because of pareto principle
    # too_much_wait = (datetime.now() - self.last_status_update_time).total_seconds() >= max_wait
    too_much_wait=False
    should_check = not force and (len(self.pending_queries)/self.max_concurrency) < update_threshold
    
    if should_check or too_much_wait:
      return self.pending_queries

    self.pending_queries = self.filter_for_pending(self.pending_queries, sleep_secs=self.sleep_secs)
    self.last_status_update_time = datetime.now()
    return self.pending_queries

  def ensure_concurrency_limit(self, **kwargs):
    max_concurrency = kwargs.get("max_concurrency", self.max_concurrency)
    while len(self.update_pending_queries()) >= max_concurrency:
      time.sleep(self.sleep_secs)
          
  def drain_completely(self):
    """Drains pending_queries to zero"""
    self.ensure_concurrency_limit(max_concurrency=0)


  def filter_for_pending(self, queries, retry_failures=True, sleep_secs=2):
    """
        This function filters an array of AthenaQueries and returns
        only non-succeeded includes a single failure retry mechanism.
        will raise an error if a query fails twice in a row.


        Note: I'm keeping track of query.retried boolean.
        Otherwise, failed queries would never get filtered out.
    """
    result = []
    for q in queries:
      status = q.status().lower()

      if retry_failures and status == "failed" and not q.retried:
        # execute a retry only before blowing up
        
        q.retried = True            
        warnings.warn(f"retrying failed query: {q.id}\n{q.state_change_reason()}")
        time.sleep(self.sleep_secs*30)
        query = AthenaQuery(q.sql)
        query.execute()  # again
        query.wait(max_tries=10000)
        status = query.status()
        if status == "failed":
          self.failures.append(q)
          raise ValueError(q.id + " failed")

      if status not in ["succeeded", "failed"]:
          result.append(q) # pending/queued
      else: # completed/cancelled/failed
          with open(self.log_path, "a") as fd:
            fd.write(dt.now().strftime("%Y-%m-%d-%T") + "\t" + q.id + "\n")
    return result
  
  def build_query(self, *args, **kwargs):
    return AthenaQuery(*args, **kwargs)
  
  def clean_results(self, bucket='stock.ai', prefix='results/'):
    """completely cleans out results folder"""
    bucket = self.s3.Bucket(bucket)
    bucket.objects.filter(Prefix=prefix).delete()
