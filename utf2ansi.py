#encoding:utf-8
'''
Created on 2016年1月14日

@author: pan
'''


import os

def convertEncoding(from_encode,to_encode,old_filepath,target_file):
    f1=file(old_filepath)
    content2=[]
    content2.append("//flag: convert utf-8 to ASNI\n") #在文件首部标记转换
    while True:
        line=f1.readline()
#        print line
        content2.append(line.decode(from_encode).encode(to_encode))
        if len(line) ==0:
            break

    f1.close()
    
#    print line
    f2=file(target_file,'w')
    f2.writelines(content2)
    f2.close()

#把文件由GBK编码转换为UTF-8编码，也就是filepath的编码是GBK
def convertFromGBK2utf8(filepath):
    convertEncoding("GBK", "UTF-8", filepath, filepath+".bak")


#把文件由UTF-8编码转换为GBK编码，也就是filepath的编码是UTF-8
def convertFromUTF82gbk(filepath):
    convertEncoding("UTF-8", "GBK", filepath, filepath)
    print "convert success"

#打印rootDir目录下的树形结构
def tree_in_python(rootDir, level=1): 
    if level==1: print rootDir 
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 
        print '│  '*(level-1)+'│--'+lists 
        if os.path.isdir(path): 
            tree_in_python(path, level+1) 

#打印rootDir目录下的所有文件名
def list_file(rootDir): 
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs: 
#         for d in dirs: 
#             print os.path.join(root, d)      
        for f in files:   
            print os.path.join(root, f) 

#转换目录下所有的.c或者.h文件，方便sourceInsight阅读源代码
def convert_utf_2_asni(srcDir):
    list_dirs = os.walk(srcDir) 
    for root, dirs, files in list_dirs:     
        for f in files: 
            if f.endswith(".c") or f.endswith(".h"):
                filename = os.path.join(root,f)
                print filename
                convertFromUTF82gbk(filename)
    
            

# filepath="G:\\code\\opensource_code\\libevent_asni\\libevent-2.0.22-stable\\buffer.c"
# filepath="utf_test.tx"
# convertFromUTF82gbk(filepath)

#转换该目录下所有.c或者.h文件，从UTF-8到GBK,方便sourceInsight阅读源代码
convert_utf_2_asni("G:\code\opensource_code\libevent_asni\libevent-2.0.22-stable")
