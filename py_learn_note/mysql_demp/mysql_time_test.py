#encoding:utf-8
'''
Created on 2015年12月5日

@author: pan
@attention: 测试mysql的插入速度
'''

import MySQLdb
import datetime
conn = MySQLdb.connect(
        host = 'localhost',
        port=3307,
        user='root',
        passwd='shadow',
        db='test',)
cur=conn.cursor()

#测试时间开始
starttime = datetime.datetime.now()
try:
    for i in range(1,1000000):
        print i
        cur.execute('insert into test2(id,name) values(%d,"testest123")' % (i))
except:
    print "error"
    conn.rollback()

conn.commit()
#测试时间结束
endtime = datetime.datetime.now()
print (endtime - starttime).seconds

conn.close()
    

    