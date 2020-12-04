
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# 定义数据
x= np.arange(1,20,1)


# 1.带标签图
plt.figure()
plt.plot(x,x**2)#,label='Fast')#label为标签
plt.plot(x,x*2)#,label='Mormal')#l
plt.legend(['Fast','Mormal'])#
plt.show()




# 2.带网格图
fig = plt.figure()
ax=fig.add_subplot()
# 在一个图表里显示两根折线
plt.plot(x,x**2,label='y')
plt.plot(x,x*2,label='yr')
# 写谁隐藏谁
plt.grid(axis="x")
ax.legend()
plt.title('test2')
plt.show()


# 3.简易画线
plt.figure()
# (3, 2, 2)表示将面板划分为3行2列，当前图像放在第2顺位
plt.subplot()
# 在一个图表里显示两根折线
plt.plot(x**2)
plt.plot(x*2)
plt.title('test')
plt.show()


# 画间断的折线图
x=[1,2,3,4,5,6,7,8]
y=[1,2,np.nan,4,5,6,np.nan,np.nan]

plt.figure()
plt.plot(x,y)#,label='Fast')#label为标签
#plt.plot(x,x*2)#,label='Mormal')#l
plt.legend(['Fast'])#
plt.show()