#! /usr/bin/env python
#coding=utf-8
#*******************************************
# 重新转换试卷文档
#*******************************************
import os,sys
import pymssql


#数据库连接
conn = pymssql.connect(host ="172.19.41.85",database ="TQMS2",user="sa",password="Founder123")

#定义游标
cur = conn.cursor()

cur.execute(
"""
update dom_5_doclib
set PAPER_EXPORTFLAG = 0
""")
conn.commit()
print "done"
#关闭数据库连接
conn.close()
