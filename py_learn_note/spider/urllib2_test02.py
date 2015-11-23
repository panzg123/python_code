#encoding:utf-8
import urllib2
#定义request对象来映射http请求
request =  urllib2.Request('http://www.baidu.com')
#返回response对象
response = urllib2.urlopen(request)
page_content=response.read()
print page_content