# -*- coding: utf-8 -*-
import os, sys
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib
import math

#if len(sys.argv) ==2:
#    code = sys.argv[1]
#else:
#    print('usage: python talib_sar.py stockcode ')
#    sys.exit(1)
# 
#if len(code) !=6:
#    print('stock code length: 6')
#    sys.exit(2)
code = "002153"
df = ts.get_k_data(code)
df1 = df[ df['date'] > '2020-01-01']
print(df1)
if len(df) <10:
    print(" len(df) <10 ")
    sys.exit(2)

print(df1.values[:,2].tolist())
print(df1.values.tolist())
# SAR，Stop and Reverse，是 Welles Wilder发明的，SAR是一个基于价格/时间的指标.
sar = talib.SAR(df1.high, df1.low)
#print(sar[-100:])
print(sar)
strr = sar.values.tolist()
str1 = ""
for i in strr:
    if math.isnan(i):
        pass
    else:
        str1 += str(i)+","
df['ma10'] = df['close'].rolling(window=10).mean()
df.index = pd.to_datetime(df.date)
# 画股票收盘价图 , SAR 散点图
df[['close','ma10']].plot(grid=True, title=code)
plt.plot(df.index, sar, '.',c='black', label='sar')
plt.legend(loc='best', shadow=True)
#plt.show()