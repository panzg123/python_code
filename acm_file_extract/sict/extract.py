# coding=utf-8
import os.path
rootdir ="E:\\baiduyun_download\\python\\acm_code"                               # 指明被遍历的文件夹

for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for dirname in  dirnames:                       #输出文件夹信息
        print "parent is:" + parent
        print  "dirname is" + dirname
    for filename in filenames:
        print "parent is:" + parent
        print "filename is:" + filename
        print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息