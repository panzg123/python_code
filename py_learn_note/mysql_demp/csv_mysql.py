#encoding:utf-8
'''
Created on 2016年3月3日

@author: pan
@attention: 从csv文件中读取数据，写入MySQL
'''
import MySQLdb
import datetime
import csv

def csv_import_mysql():
    conn = MySQLdb.connect(
        host = 'localhost',
        port=3307,
        user='root',
        passwd='shadow',
        db='dkl',)
    cur=conn.cursor()
    #获取csv数据
    reader = csv.reader(file('new_datetime_mysql.csv', 'rb'))
    try:
        #读取每行数据，写入数据
        for line in reader:
            print line
            str = "insert into datetime_test(id,time,value) values(%s,\"%s\",%s)" % (line[0],line[1],line[2])
            print str
            cur.execute(str)
            
    except:
        print "error"
        conn.rollback()
    #提交，关闭连接
    conn.commit()
    conn.close()
    
    
csv_import_mysql()