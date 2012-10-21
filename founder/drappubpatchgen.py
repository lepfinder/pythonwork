#! /usr/bin/env python
#coding=utf-8
#*******************************************
# drappub 补丁生成器
# 根据类的全限定名找到指定的class文件，拷贝出来
#/TQMS/WebRoot/product/CheckUpdateName.jsp
#/TQMS/src/com/founder/qlib/common/util/FtpClient.java
#*******************************************

import os,shutil
import os.path

#patchdir = raw_input("patch path:")
patchdir = "I:/DRAP_PATCH"

listfile = os.path.join(patchdir,"drappub.txt")

if(os.path.exists(patchdir+"/drappub")):
    print "exists drappub,delete first"
    shutil.rmtree(patchdir+"/drappub")

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
        
        srcfile = filename.replace("/drappub/WebRoot","D:/apache-tomcat-6.0.26/webapps/drappub")
        srcfile = srcfile.replace("/drappub/src","D:/apache-tomcat-6.0.26/webapps/drappub/WEB-INF/classes")
        srcfile = srcfile.replace(".java",".class")
        
        destDir = filename.replace("/drappub/WebRoot","/drappub")
        destDir = destDir.replace("/drappub/src","/drappub/WEB-INF/classes")
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
else:
    print "can't find",listfile
