import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
today = date.today()
import datetime 
tod = datetime.datetime.now()
d = datetime.timedelta(days = 14)
a = tod - d
a=str(a)
a=a[:10]
today = today.strftime("%Y/%m/%d")
from pandas_datareader import data
#stocks = data.DataReader(['ADANIPORTS.NS','ASIANPAINT.NS','BAJFINANCE.NS','BAJAJFINSV.NS'], 'yahoo', start='2020/03/14', end='2021/03/14')
stocks = data.DataReader(['ADANIPORTS.NS','ASIANPAINT.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BHARTIARTL.NS','BPCL.NS','BRITANNIA.NS','CIPLA.NS','COALINDIA.NS','DIVISLAB.NS','DRREDDY.NS','EICHERMOT.NS','GRASIM.NS'    ,'HCLTECH.NS','HDFC.NS','HDFCBANK.NS','HDFCLIFE.NS','HEROMOTOCO.NS','HINDALCO.NS','HINDUNILVR.NS','ICICIBANK.NS','INDUSINDBK.NS','INFY.NS','IOC.NS','ITC.NS','JSWSTEEL.NS','KOTAKBANK.NS','LT.NS','M&M.NS','MARUTI.NS','NESTLEIND.NS','NTPC.NS','ONGC.NS','POWERGRID.NS','RELIANCE.NS','SBIN.NS','SBILIFE.NS','SHREECEM.NS','SUNPHARMA.NS','TATAMOTORS.NS','TATASTEEL.NS','TATACONSUM.NS','TCS.NS','TECHM.NS','TITAN.NS','ULTRACEMCO.NS','UPL.NS','WIPRO.NS'], 'yahoo', start=a, end=today)
O=stocks['Open']
C=stocks['Close']
R=(C-O)/O
print(R)