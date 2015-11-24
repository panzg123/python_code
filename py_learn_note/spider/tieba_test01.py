#encoding:utf-8
import string,urllib2
#定义百度函数
def baidu_tieba(url,begin_page,end_page):
    for i in range(begin_page,end_page+1):
        sName=string.zfill(i, 5)+'.html'
        print '正在下载'+str(i)+'个网页，并存为文件'+sName
        f=open(sName,'w+')
        m=urllib2.urlopen(url+str(i)).read()
        f.write(m)
        f.close()
#抓取这个网址的1-10页，保存为html文件        
bdurl = 'http://tieba.baidu.com/p/2296017831?pn='  
iPostBegin = 1  
iPostEnd = 10  

baidu_tieba(bdurl,iPostBegin,iPostEnd)  