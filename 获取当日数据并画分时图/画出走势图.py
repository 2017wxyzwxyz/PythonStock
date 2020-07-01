import matplotlib.pyplot as plt
import pdb
import numpy as np
import csv
import time

def PlotDemo1(a, b):
    a1 = []
    b1 = []
    a1 = a
    b1 = b
    fig  = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(a,b)
    plt.show()

  

def PlotDemo(a,zero):
    a1 = []
    b1 = []
    a1 = a
    fig  = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(a)
    ax.plot(zero)
    plt.show()  
    
 


def Run(symbol):
    csv_reader = csv.reader(open("E:/MyGit/PythonStock/获取当数据并画分时图/data/"+time.strftime('%Y%m%d')+"/"+symbol+".csv",'r', encoding='utf-8'))
    #pdb.set_trace()
    PICES1 = [row[4] for row in csv_reader]
    csv_reader1 = csv.reader(open("E:/MyGit/PythonStock/获取当数据并画分时图/data/"+time.strftime('%Y%m%d')+"/"+symbol+".csv",'r', encoding='utf-8'))
    TIME1 = [row[10] for row in csv_reader1]
    csv_reader2 = csv.reader(open("E:/MyGit/PythonStock/获取当数据并画分时图/data/"+time.strftime('%Y%m%d')+"/"+symbol+".csv",'r', encoding='utf-8'))
    yesterday = [row[3] for row in csv_reader2][2]
    
    TIME2 = [row[4] for row in csv_reader]
    PICES3 = [row[5] for row in csv_reader]
    TIME3 = [row[6] for row in csv_reader]
    PICES4 = [row[7] for row in csv_reader]
    TIME4 = [row[8] for row in csv_reader]
    PICES5 = [row[9] for row in csv_reader]
    TIME5 = [row[10] for row in csv_reader]
    
    print(PICES1)
    print(TIME1)
    print( yesterday)
    print(TIME2)
    print(PICES3)
    print(TIME3)
    print(PICES4)
    print(TIME4)
    print(PICES5)
    print(TIME5)
    #PlotDemo1()
    #res = [x-1 for x in PICES1]
    a = PICES1.remove('当前价格')
    b = TIME1.remove('时间')
    print(PICES1)
    res = list(map(float,PICES1))
    res = [x-float(yesterday) for x in res]
    res = [x/float(yesterday)*100 for x in res]
    zero = [0 for i in range(len(res))]
    print(zero)
    print(TIME1)
    PlotDemo(res,zero)


if __name__ == '__main__':
    Run("300736")

