# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:03:03 2021

@author: Dell
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data
#stocks = data.DataReader(['ADANIPORTS.NS','ASIANPAINT.NS','BAJFINANCE.NS','BAJAJFINSV.NS'], 'yahoo', start='2020/03/14', end='2021/03/14')
stocks = data.DataReader(['ADANIPORTS.NS','ASIANPAINT.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BHARTIARTL.NS','BPCL.NS','BRITANNIA.NS','CIPLA.NS','COALINDIA.NS','DIVISLAB.NS','DRREDDY.NS','EICHERMOT.NS','GRASIM.NS'    ,'HCLTECH.NS','HDFC.NS','HDFCBANK.NS','HDFCLIFE.NS','HEROMOTOCO.NS','HINDALCO.NS','HINDUNILVR.NS','ICICIBANK.NS','INDUSINDBK.NS','INFY.NS','IOC.NS','ITC.NS','JSWSTEEL.NS','KOTAKBANK.NS','LT.NS','M&M.NS','MARUTI.NS','NESTLEIND.NS','NTPC.NS','ONGC.NS','POWERGRID.NS','RELIANCE.NS','SBIN.NS','SBILIFE.NS','SHREECEM.NS','SUNPHARMA.NS','TATAMOTORS.NS','TATASTEEL.NS','TATACONSUM.NS','TCS.NS','TECHM.NS','TITAN.NS','ULTRACEMCO.NS','UPL.NS','WIPRO.NS'], 'yahoo', start='2020/03/14', end='2021/03/14')

stocks=stocks['Adj Close']
log_ret =np.log(1+stocks.pct_change())
np.random.seed(42)
num_ports = 1
all_weights = np.zeros((num_ports, len(stocks.columns)))
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)


weights=[1/50]*50
weights=pd.DataFrame(weights)
ret_arr = np.sum((log_ret.mean() * (1/50) * 250))
vol_arr = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*250,weights)))
    
print("Annaul Returns of each stock in an equally waited portfolio: ", log_ret.mean()*(1/50)*250)








