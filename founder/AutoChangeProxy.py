#! /usr/bin/env python
#coding=utf-8
#*******************************************
#
#HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings
#*******************************************
import win32api,win32con
import time,shutil,os

#通过修改注册表中的值，切换IE是否使用代理
def changeIEProxy(keyName,keyValue):
    pathInReg = 'Software\Microsoft\Windows\CurrentVersion\Internet Settings'

    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,pathInReg,0,win32con.KEY_ALL_ACCESS)
    win32api.RegSetValueEx(key,keyName,0,win32con.REG_DWORD,keyValue)
    win32api.RegCloseKey(key)

#根据公司或家里环境，切换SVN代理
def changeSvnProxy(env):
    path = 'C:\\Users\\xiyang\\AppData\\Roaming\\Subversion\\'
    #at work
    if env:
        print "copy server-work"
        shutil.copy2(os.path.join(path,"servers-work"),os.path.join(path,"servers"))
    else: #at home
        print "copy server-home"
        shutil.copy2(os.path.join(path,"servers-home"),os.path.join(path,"servers"))
        
if __name__ == "__main__":
    pathInReg = 'Software\Microsoft\Windows\CurrentVersion\Internet Settings'
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,pathInReg,0,win32con.KEY_ALL_ACCESS)
    value,type = win32api.RegQueryValueEx(key,'ProxyEnable')
    #print value
    
    if value == 1:
        value = 0
        print "at home,disable proxy"
    else:
        value = 1
        print "at work,enable proxy!"
    
    time.sleep(1)
    changeSvnProxy(value)
    time.sleep(1)
    changeIEProxy('ProxyEnable',value)
    print "done"

