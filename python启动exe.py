#coding=utf-8
import subprocess
subprocess.call(["C:/Users/Administrator/Desktop/Debug1/test.exe","asdfg"])
#pname = "C:/Users/Administrator/Desktop/Debug/test.exe"
#source=b"asdfghjk"
#p = subprocess.Popen(pname, stdin=subprocess.PIPE,stdout=subprocess.PIPE)
#result = p.communicate(input=source)
#res = result[0].decode()[0:leng]
#print(res)




import win32api
#日报软件启动
#win32api.ShellExecute(0, 'open', r'C:\Users\Administrator\Desktop\Debug\test.ece', '','',1)

import os
import win32process
#os.startfile("C:/Users/Administrator/Desktop/Debug/test.exe")
#win32process.CreateProcess('C:/Users/Administrator/Desktop/Debug/test.exe', '', None, None, 0, win32process.CREATE_NO_WINDOW,None, None, win32process.STARTUPINFO())




import win32event
handle = win32process.CreateProcess('C:/Users/Administrator/Desktop/Debug1/test.exe',
                                    "C:/Users/Administrator/Desktop/Debug1/test.exe 这是啥", None, None, 0,
win32process.CREATE_NEW_CONSOLE, None, None, win32process.STARTUPINFO())
win32event.WaitForSingleObject(handle[0], -1)
handle = win32process.CreateProcess('C:/Users/Administrator/Desktop/Debug1/test.exe',
                                    "C:/Users/Administrator/Desktop/Debug1/test.exe 结束了", None, None, 0,
win32process.CREATE_NEW_CONSOLE, None, None, win32process.STARTUPINFO())


