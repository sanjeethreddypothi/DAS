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
num_ports = 10000
all_weights = np.zeros((num_ports, len(stocks.columns)))
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)

for x in range(num_ports):
    # Weights
    weights = np.array(np.random.random(len(stocks.columns)))
    weights = weights/np.sum(weights)
    
    # Save weights
    all_weights[x,:] = weights
    
    # Expected yearly-return
    ret_arr[x] = np.sum((log_ret.mean() * weights * 252))
    vol_arr[x] = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*250, weights)))
    
    # Sharpe Ratio
    sharpe_arr[x] = ret_arr[x]/vol_arr[x]
print("Gloabal Minimum Variance in the array: {}".format(vol_arr.min()))
print("It's location in the array: {}".format(vol_arr.argmin()))

print("Max Sharpe Ratio in the array: {}".format(sharpe_arr.max()))
print("It's location in the array: {}".format(sharpe_arr.argmax()))
print("Weights of each stock in the portfolio ",all_weights[sharpe_arr.argmax(),:])

glob_ret=ret_arr[vol_arr.argmin()]
glob_vol=vol_arr[vol_arr.argmin()]

max_sr_ret = ret_arr[sharpe_arr.argmax()]
max_sr_vol = vol_arr[sharpe_arr.argmax()]



plt.figure(figsize=(15,8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='viridis')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.scatter(max_sr_vol, max_sr_ret,c='red', s=50) # red dot
plt.scatter(glob_vol, glob_ret,c='orange', s=50) # red dot
plt.show()


