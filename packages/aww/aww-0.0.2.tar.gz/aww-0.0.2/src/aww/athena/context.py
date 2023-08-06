import pandas as pd
import boto3
from pathlib import Path
from .query_manager import AthenaQueryManager

def init_tickers_from_file(path="data/tickers.csv"):
    df = pd.read_csv(path)
    return list(df['ticker'])

class Context():
  """
  Object with module level scope
  
  kwargs are passed to following objects:
  * AthenaQueryManager
  """
  def __init__(self, **kwargs):
    self.s3 = kwargs.pop("s3",  boto3.resource("s3"))
    self.qm = AthenaQueryManager(s3=self.s3, **kwargs)

    if kwargs.get("tickers") is None:
        path = Path(__file__).parent.parent.parent/"data"/"tickers.csv" # /home/m/code/stock/data/tickers.csv
        print("loading tickers from path", path)
        self.tickers = init_tickers_from_file(kwargs.get("ticker_file", path))
    else:
        self.tickers = kwargs.get("tickers")
    self.failed = []

