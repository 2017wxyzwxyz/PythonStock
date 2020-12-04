import tushare as ts
import matplotlib.pyplot as plt
import mpl_finance as mpf
import numpy as np
data = ts.get_k_data('002153', ktype='D', autype='qfq', start='2019-12-17', end='')
prices = data[['open', 'high', 'low', 'close']]
dates = data['date']
candleData = np.column_stack([list(range(len(dates))), prices])
fig = plt.figure(figsize=(10, 6))
ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
mpf.candlestick_ohlc(ax, candleData, width=0.5, colorup='r', colordown='b')
plt.savefig('D:\\workspace\\Python_Test\\导出的图片.png')
plt.show()
