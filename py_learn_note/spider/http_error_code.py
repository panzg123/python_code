#encoding:utf-8
from urllib2 import Request, urlopen, URLError, HTTPError

#geturl方法，返回获取的真实的URL
old_url = 'http://rrurl.cn/b1UZuP'
req = Request(old_url)
response = urlopen(req)
print 'Old url :' + old_url
print 'Real url :' + response.geturl()

#info方法，返回对象的字典对象
print 'Info():'  
print response.info()