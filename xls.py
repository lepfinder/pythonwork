#############################################################
# file: xls.py
# brief: use xlrd process office excel files 
# author: xiyang
# date: 12/04/04
# changleLists:
#
#############################################################

#! /usr/bin/env python
#coding=utf-8
import xlrd
import os,os.path

#define the directory
DATA_PATH = r'D:\test'

files = os.listdir(DATA_PATH)
data = {}

def extraRecord(filepath):
    bk = xlrd.open_workbook(filepath)
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name('Sheet1')
    except:
        print "no sheet in %s named Sheet1" % fname
        return None
    
    nrows = sh.nrows
    ncols = sh.ncols
    
    for i in range(3,nrows):
        row_data = sh.row_values(i)
        if row_data[2]:
            l = []
            name = row_data[1]
            #sdut
            l.append(row_data[2])
            #pku
            l.append(row_data[4])
            #hdu
            l.append(row_data[6])
            #bauu
            l.append(row_data[8])
            #zju
            l.append(row_data[10])
            #hru
            l.append(row_data[12])
            data[name] = l
            print "->"+name+":",data[name]

# traverse  
for file in files:
    if os.path.isfile:
        #get the file's ext
        temp = os.path.splitext(file)
        ext = temp[1]
        if ext == '.xls':
            #print os.path.join(DATA_PATH,file)
            extraRecord(os.path.join(DATA_PATH,file))



        
    
        
        
        


