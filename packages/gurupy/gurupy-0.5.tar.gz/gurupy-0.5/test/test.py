import pandas as pd
import setuptools
import gurupy
from dotenv import load_dotenv
import os


# Set variables
load_dotenv()
token = os.getenv('gt')
ticker = 'txn'


x = gurupy.stock_financials_annual_df(token, ticker)
print(x)
print(x.columns)



