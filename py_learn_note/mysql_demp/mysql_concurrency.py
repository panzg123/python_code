#coding=utf-8
'''
Created on 2015年12月7日

@author: pan
@attention: 模拟100个mysql连接，同时插入100个10kb长度的记录
'''

import MySQLdb
import datetime
import threading

#从test.txt中读取要插入的数据
def read_file(filepath):
    file_object = open(filepath)  
    try:  
        all_the_text = file_object.read()  
    finally:  
        file_object.close()
    return all_the_text

file_content = read_file('../test.txt')
#计时器开始
starttime = datetime.datetime.now()
#测试
def move():
    print "test:"
#线程工作函数
def mysql_write():
    #连接mysql
    conn = MySQLdb.connect(
        host = 'localhost',
        port=3307,
        user='root',
        passwd='shadow',
        db='test',
        charset='utf8')  #这里一定要指明utf8连接，否则插入出现乱码
    cur=conn.cursor()
    try:
        for i in range(1,101):
            print i
            sql_content = "insert into test(id,name,name2) values(%d,'%s','%s')" % (i,file_content,file_content)
            cur.execute(sql_content)
            #sleep(0.01)
    except:
        print "error"
        conn.rollback()
    conn.commit()
    conn.close()
    print "done"
#创建线程    
threads = []
for i in range(1,101):
    t=threading.Thread(target=mysql_write)
    threads.append(t)
#线程开始
for i in range(0,100):
    threads[i].start()
#等待主线程
for i in range(0,100):
    threads[i].join()
    

#计时器结束
endtime = datetime.datetime.now()
print 'time:',(endtime - starttime).seconds    