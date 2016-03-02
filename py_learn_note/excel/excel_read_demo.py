#-*- coding: utf8 -*-
'''
Created on 2016年3月2日

@author: pan
'''
import xlrd

#打开文件
def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

#逐行读取，打印
def read_demo():
    fname = "file.xls"
    bk = xlrd.open_workbook(fname)
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print "no sheet in %s named Sheet1" % fname
    #获取行数
    nrows = sh.nrows
    #获取列数
    ncols = sh.ncols
    print "nrows %d, ncols %d" % (nrows,ncols)
    #获取第一行第一列数据 
    cell_value = sh.cell_value(1,1)
    #print cell_value

    row_list = []
    #获取各行数据
    for i in range(1,nrows):
        row_data = sh.row_values(i)
        print row_data
        row_list.append(row_data)
        
#如果一个xls文件有多个表格，则可以根据索引来读取
#reference：http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html
#根据索引获取Excel表格中的数据   
#参数:file：Excel文件路径     
#colnameindex：表头列名所在行的所以
#by_index：表的索引
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
             list.append(app)
    return list