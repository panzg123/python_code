# coding=utf-8
import os.path
import sys, shutil, os, string
rootdir ="F:\\acm_code"
destDir = "F:\\acm_code_merge"

def cpFile(srcPath):
    fileName = os.path.basename(srcPath)
    destPath = destDir + os.path.sep + fileName
    if os.path.exists(srcPath) and not os.path.exists(destPath):
        print 'cp %s %s' % (srcPath,destPath)
        shutil.copy(srcPath,destPath)
def getDir(my_filepath):
    dir = my_filepath.split('\\')
    return dir[2]


def extract():
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:
            print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
            if filename.endswith(".c") or filename.endswith(".cpp"):
                filepath=os.path.join(parent,filename)
                pre_dir_name = getDir(filepath)
                cpFile(filepath)
                os.rename(destDir+"\\"+filename, destDir+"\\"+pre_dir_name+"_"+filename)

extract()