#encoding:utf-8
import urllib2
import cookielib

#设置代理
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler=urllib2.ProxyHandler({})
if enable_proxy:
    opener=urllib2.build_opener(proxy_handler)
else:
    opener=urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

#设置超时时间
#urllib2.socket.setdefaulttimeout(10)
#或者在urllib2.urlopen中直接设置timeout参数
#urllib2.urlopen('url',timeout=10)

#cookie的读取
cookie=cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response=opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name='+item.name
    print 'Value='+item.value
