#encoding:utf-8
#python通过urllib2模拟浏览器Get请求
import urllib
import urllib2

data={}
data['username']='123'
data['passwd']='123'
url_value = urllib.urlencode(data)
print url_value

url = 'http://localhost/chatroom/LoginController.php'
full_url=url+'?'+url_value

#data=urllib2.open(full_url)


