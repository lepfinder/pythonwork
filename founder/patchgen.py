#! /usr/bin/env python
#coding=utf-8
#*******************************************
# TQMS 补丁生成器
# 根据类的全限定名找到指定的class文件，拷贝出来
#/TQMS/WebRoot/product/CheckUpdateName.jsp
#/TQMS/src/com/founder/qlib/common/util/FtpClient.java
#*******************************************

import os,shutil
import os.path

#patchdir = raw_input("patch path:")
patchdir = "C:/TQMS_PATCH"

listfile = os.path.join(patchdir,"tqms.txt")

if(os.path.exists(patchdir+"/TQMS")):
    print "exists TQMS,delete first"
    shutil.rmtree(patchdir+"/TQMS")

if(os.path.exists(listfile)):
    print listfile
    file = open(listfile)
    for filename in file:
        if filename[0] == '#':
            print "comment:",filename
            continue
        if filename[-1] == '\n':
            filename = filename[0:-1]
            
        if filename == '':
            continue
        
        filename = filename.replace("TQMS2.0","TQMS")
        srcfile = filename.replace("/TQMS/WebRoot","D:/Tomcat5.5/webapps/TQMS")
        srcfile = srcfile.replace("/TQMS/src","D:/Tomcat5.5/webapps/TQMS/WEB-INF/classes")
        srcfile = srcfile.replace(".java",".class")
        
        destDir = filename.replace("/TQMS/WebRoot","/TQMS")
        destDir = destDir.replace("/TQMS/src","/TQMS/WEB-INF/classes")
        destDir = destDir.replace(".java",".class")
        destDir = patchdir + os.path.dirname(destDir);
        
        if(not os.path.exists(destDir)):
            print "make dirs:",destDir
            os.makedirs(destDir)
            
        if(os.path.exists(srcfile)):
            print "copy file:",filename
            shutil.copy2(srcfile,destDir)
        else:
            print "cant find file:",filename

