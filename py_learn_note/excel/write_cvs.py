#encoding:utf-8
'''
Created on 2016年3月2日

@author: pan
'''

#引入csv模块
import csv

#写入，向your.csv文件中写入5行3列数据
def write_csv():
    writer = csv.writer(file('your.csv', 'wb'))
    writer.writerow(['Column1', 'Column2', 'Column3'])
    lines = [range(3) for i in range(5)]
    for line in lines:
        writer.writerow(line)

#读取打印csv文件中的每一行数据
def read_csv():
    reader = csv.reader(file('distinct_datetime3.csv', 'rb'))
    for line in reader:
        print line

#csv文件中第一列是时间属性，该函数的目的是在时间前后加中括号，如2015-12-03改为[2015-12-03]
#最后另存为到new_datetime.csv中
def read_and_write():
    reader = csv.reader(file('distinct_datetime3.csv', 'rb'))
    writer = csv.writer(file('new_datetime.csv', 'wb'))
    for line in reader:
        row_value=[]
        time="["
        time+=line[0]
        time+="]"
        row_value.append(time)
        row_value.append(line[1])
        writer.writerow(row_value)
        
read_and_write()