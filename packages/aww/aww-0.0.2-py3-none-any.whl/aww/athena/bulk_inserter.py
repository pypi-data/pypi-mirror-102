import requests
import time
import traceback
from tqdm.auto import tqdm as tqdm # threadsafe fix
from .athena_query import AthenaQuery

class BulkInserter():
  """
  Service object that handles logic for the following:
    * creating tables if not exist
    * waiting for partitions to be created
    * waiting for hive metadata to be updated after table/partition creation
    * error handling

  Required keyword arguments:
    * Context: context.Context() object that contains AthenaQueryManager
    * query_func: function takes an individual item from list and returns an AthenaQuery

  Optional keyword arguments:
    * create_table_query_func
    * skip_table_create: skips creating table on first item
  """

  def __init__(self, **kwargs):
    self.ctx = kwargs["ctx"]
    self.query_func = kwargs["query_func"]
    self.iterable = kwargs.get("iterable")
    self.skip_table_create = kwargs.get("skip_table_create", False)
    self.create_table_query_func = kwargs.get("create_table_query_func")

    if not self.skip_table_create and self.create_table_query_func is None:
        raise KeyError("'create_table_query_func' - You can also disable creating a table by passing skip_table_create=True")

    self.error_func = kwargs.get("error_func")
    self.send_error_notifications = kwargs.get("send_error_notifications", True)
    self.ifttt_error_endpoint = kwargs.get(
        "ifttt_error_endpoint", "https://maker.ifttt.com/trigger/automation_alert/with/key/bkB3Sd8MCxAcZQNbr6X1XI")

    self.desc = kwargs.get("desc")
    
  def execute(self, iterable=None, idx=None, **kwargs):
    """
    Takes an iterable and passes each item to `self.query_func`.
    Defaults to using self.iterable. You can optionally pass a specific iterable if desired.
    
    idx is considered the index for a LIST of 2D ticker ranges. See `collect_date_range_iterables`.

    For the first item only, this will create a table by calling
     `self.create_table_query_func` unless `self.skip_table_create = True`.

    Errors are passed to `self.error_func` if present with arguments error, item. 
    """
    if iterable is None:
      iterable = self.iterable
      
    skip_table_create = kwargs.get("skip_table_create", self.skip_table_create) 
    desc = kwargs.get("desc", self.desc)
    is_batch = kwargs.get("is_batch", False)
    disable_progress = kwargs.get("disable_progress", False)
    leave_progress = kwargs.get("leave_progress", True)
      
    is_2d_array = isinstance(iterable[0], list)
    if is_2d_array:
      assert idx is not None

    self.started_at = time.time()

    counter = 0
    for x in tqdm(iterable, desc=desc, disable=disable_progress, leave=leave_progress):
      if is_2d_array:
        idx = counter
      
      if idx == 0 and not skip_table_create:
        query = self.create_table_query_func(x)
      else:
        query = self.query_func(x)

      self.ensure_it_is_athena_query(query)

      try:
        should_wait = idx == 0 and not skip_table_create and not is_batch # wait for partitions to be created on first item
        self.ctx.qm.execute_query(query, wait=should_wait)
      except Exception as err:
        self.handle_error(err, query)
      finally:
        counter += 1

    self.completed_at = time.time()
    self.duration = self.completed_at - self.started_at
    return dict(duration=self.duration, items=counter)

  def ensure_it_is_athena_query(self, obj):
    instance = type(obj)
    if not isinstance(obj, AthenaQuery):
      raise TypeError("expected an AthenaQuery but got {}".format(instance))

  def handle_error(self, err, item, verbose=False, sleep_secs=5):
    self.ctx.failed.append(item) # NOTE: there is also a collection in QueryManager.failures

    if self.error_func is not None:
      return self.error_func(err, item)

    # default error handling
    print("!!!! caught error for item", item)
    if verbose:
        print(traceback.print_exc())
    else:
        print(err)

    if not isinstance(err, ValueError):
      self.send_notification(self.ifttt_error_endpoint, "BulkInserter: critical exception occurred for item", str(item))

    time.sleep(sleep_secs)


  def send_notification(self, url, value1=None, value2=None, value3=None):
    res = requests.post(url, json=dict(value1=value1, value2=value2, value3=value3))
    assert res.status_code >= 200
    return res
