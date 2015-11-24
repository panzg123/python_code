#encoding:utf-8
#从丑事百科网站上抓取内容，保存到文本中
import re
import urllib2
import string

def GetPage(page,sName):  
        myUrl = "http://m.qiushibaike.com/hot/page/" + str(page)
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
        headers = { 'User-Agent' : user_agent } 
        req = urllib2.Request(myUrl, headers = headers) 
        myResponse = urllib2.urlopen(req)
        myPage = myResponse.read()  
        #encode的作用是将unicode编码转换成其他编码的字符串  
        #decode的作用是将其他编码的字符串转换成unicode编码  
        #unicodePage = myPage.decode("utf-8")  
  
        # 找出所有class="content"的div标记  
        #re.S是任意匹配模式，也就是.可以匹配换行符  
        myItems = re.findall('<div.*?class="content">(.*?)</div>',myPage,re.S)  
        for item in myItems:  
            print item
            f=open(sName,'a+')
            f.write(item)
            f.close() 

def save_html(begin_page,end_page):
    for i in range(begin_page,end_page):
        sName='qiushibaike/'+string.zfill(i, 5)+'.txt'
        GetPage(i, sName)
#定义起始位置和结束位置
iPostBegin = 1  
iPostEnd = 35 

save_html(iPostBegin, iPostEnd)