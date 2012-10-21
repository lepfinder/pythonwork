#! /usr/bin/env python
#coding=utf-8
#*******************************************
# 激活TQMS数据库
#*******************************************
import os,sys
import pymssql


#数据库连接
conn = pymssql.connect(host ="172.19.41.53",database ="TQMS",user="sa",password="Founder123")

#定义游标
cur = conn.cursor()

#激活题库授权为正式授权
cur.execute(
"""
update FSYS_SYSCONFIG
set value = 'BJIWN4LbzsJN4jU87UvGmrQyxpd5SKYl' 
where SYSCONFIGID = 58
""")
conn.commit()

cur.execute('SELECT * FROM FSYS_SYSCONFIG WHERE SYSCONFIGID=%d', 58)
row = cur.fetchone()
while row:
    print row[0],row[1],row[2],row[3],row[4]
    row = cur.fetchone()
#关闭数据库连接
conn.close()
