import requests
import time
import os
import json
import pdb
import numpy as np
import csv


#url = "http://hq.sinajs.cn/list=sh603007"
para = {}
header ={}
#r = requests.get(url,data=para,headers= header)
#r = str(r.content, encoding = "gbk")


def WriteTxt( message, path, filename):
    strMessage = '\n' + time.strftime('%Y-%m-%d %H:%M:%S')
    strMessage += ':\n%s' % message
    fileName = os.path.join(path, time.strftime('%Y-%m-%d') + "_" + filename +  '.txt')
    with open(fileName, 'a', encoding='utf-8') as f:
        f.write(strMessage)

#写一个Csv
def WriteCsv( message, path1, filename):
    strMessage = message + '\n'
    fileName = os.path.join(path1, filename +  '.csv')
    with open(fileName, 'a', encoding='utf-8') as f:
        f.write(strMessage)


#读取文件内容
def ReadTxt(path):
    f = open(path, 'r', encoding='utf-8')
    info = f.read()
    f.close()
    return info


#拼接要发送的http字符串
def MakeStr(arr):
    i = 1
    str = "http://hq.sinajs.cn/list="
    for item in arr:
        if i < len(arr):
            str += item + ","
        else:
            str += item
        i += 1
    return str
    

#每条股票数据写入对应的文件夹
def WriteEverySymbol(info, filePath, fileName):
    #如果数据文件存在，追加一条最新数据
    if os.path.exists(filePath + fileName + ".csv"):
        print("exists")
        WriteCsv(info, filePath, fileName)
        #pdb.set_trace()
    #如果数据不存在，创建这个文件和列名，并追加一条最新数据
    else:
        print("not exists")
        #判断文件夹是否存在，如果没有先创建文件夹
        if not os.path.exists(filePath):
            os.makedirs(filePath)
        WriteCsv("股票代码,股票名称,今日开盘价,昨日收盘价,当前价格,今日最高价,今日最低价,成交的股票数,成交金额,日期,时间",filePath,fileName)
        WriteCsv(info, filePath, fileName)
        #pdb.set_trace()


def Main():
    try:
        #读取股票代码，转换成数组
        strRead = ReadTxt("E:/MyGit/PythonStock/获取当数据并画分时图/SymbolList1.txt")
        arr = strRead.split(',')

        #拆分数组
        step = len(arr)//5 + 1
        arrs = [arr[i:i+step] for i in range(0,len(arr),step)]
        
        #使用每个拆分的数组获取数据并存储
        for n in range(len(arrs)):
            #根据数组拼接请求字符串
            str1 = MakeStr(arrs[n])
            #获取返回的请求
            r1 = requests.get(str1,data=para,headers= header)
            r1 = str(r1.content, encoding = "gbk")
            #一批返回的数据r1据转换成一个数组
            r2 = r1.split('\n')
            #每一条数据r2对应一只股票，所有数据按照股票名称和字段拆分重组后存储
            for num in range(len(r2)-1):#数据最后有一条空值去除
                r3 = r2[num].split(',')
                #print("股票代码"+r3[0][13:19])
                #print("股票名称"+r3[0][-4:])
                #print("今日开盘价"+r3[1])
				#print("昨日收盘价"+r3[2])
                #print("当前价格"+r3[3])
                #print("今日最高价"+r3[4])
                #print("今日最低价"+r3[5])
                #print("成交的股票数"+r3[8])
                #print("成交金额"+r3[9])
                #print("日期"+r3[30])
                #print("时间"+r3[31])
                info = r3[0][13:19]+","+r3[0][-4:]+","+r3[1]+","+r3[2]+"," \
                +r3[3]+","+r3[4]+","+r3[5]+","+r3[8]+","+r3[9]+","+r3[30]+","+r3[31]
                #每一个股票建立一个存储文件
                WriteEverySymbol(info, "E:/临时测试程序/DrawStock/data/"+time.strftime('%Y%m%d')+"/", info.split(',')[0])
                #pdb.set_trace()
                #print(info)
        print ("数据存储完成"+time.strftime('%Y-%m-%d %H:%M:%S'))
        #pdb.set_trace()
        #csv_reader = csv.reader(open("D:/MyGit/DrawStock/data/000002.csv",'r', encoding='utf-8'))
        #column = [row[2] for row in csv_reader]
        #print(column)
        #创建一个当日文件夹，每条数据建立一个文件，将对应数据存入文件
        #pdb.set_trace()
        #print ('\n\n\n\n\n\n\n\n\n')
    except Exception as e:
        print (e)


#执行函数
def run(interval):
    while True:
        try:
            # sleep for the remaining seconds of interval
            time_remaining = interval - time.time() % interval
            time.sleep(time_remaining)
            if ("09:25:00" < time.strftime('%H:%M:%S') < "11:30:00") or \
                    ("13:00:00" < time.strftime('%H:%M:%S') < "15:01:00"):
                Main()
            elif time.strftime('%H:%M:%S') < "09:25:00" or time.strftime('%H:%M:%S') > "15:01:00":
                print("早晚没有行情"+time.strftime('%Y-%m-%d %H:%M:%S'))
                time.sleep(300)
            else :
                print("午间没有行情"+time.strftime('%Y-%m-%d %H:%M:%S'))
            
        except Exception as e:
            print(e)
    

    
if __name__ == '__main__':
    #Main()
    run(30)







