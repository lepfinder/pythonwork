#! /usr/bin/env python
#coding=utf-8
#*******************************************
# TQMS 自动同步工具
# 本工具用来自动同步TQMS1.5和TQMS2.0代码
# 平时项目开发在TQMS1.5上进行修改，修改之后将改动的文件同步到2.0的项目上
# 思路：
#    根据更新时间，进行时间对比，提取出更改过文件列表
#*******************************************

import os,shutil,fnmatch
import os.path

srcdir = "F:\\workspace\\androidinaction\\TQMS"
destdir = "F:\\workspace\\androidinaction\\TQMS2.1"


def all_files(root,patterns='*',single_level=False,yield_folders=False):
    patterns = patterns.split(';')
    print root
    for path,subdirs,files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)
        files.sort()
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name,pattern):
                    yield (path,name)
                    break
        if single_level:
            break
 
if __name__ == '__main__':
    for path,name in all_files(srcdir,"*.java"):
        path2 = path.replace("TQMS","TQMS2.1")
        size1 = os.path.getsize(os.path.join(path,name))
        size2 = os.path.getsize(os.path.join(path2,name))
        if size1 != size2:
            print os.path.join(path,name),size1,size2
