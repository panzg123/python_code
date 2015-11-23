#!/usr/bin/python
# -*- coding: UTF-8 -*-


import MySQLdb

db = MySQLdb.connect("localhost","root","","chat")
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
 
# 创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
 
cursor.execute(sql)
 
# SQL 插入语句
sql2 = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    # 执行sql语句
    cursor.execute(sql2)
    # 提交到数据库执行
    db.commit()
except:
    #Rollback in case there is any error
    db.rollback()
    
# SQL 查询语句
sql3 = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
# 执行SQL语句
cursor.execute(sql3)
# 获取所有记录列表
results = cursor.fetchall()
for row in results:
    fname = row[0]
    lname = row[1]
    age = row[2]
    sex = row[3]
    income = row[4]
    # 打印结果
    print "fname={0%s},lname={1%s},age={2%d},sex={3%s},income={4%d}" % \
            (fname, lname, age, sex, income )
# 关闭数据库连接
db.close()