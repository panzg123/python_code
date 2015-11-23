#encoding:utf-8
#python通过urllib2提交表单数据，模拟浏览器POST请求
import urllib
import urllib2
#本地一个登陆的网站
url = 'http://localhost/chatroom/LoginController.php'
#要提交的表单数据，登陆成功将返回成功页面
values = {'username' : '123',    
          'passwd' : '1234' }    

data = urllib.urlencode(values) # 编码工作  
req = urllib2.Request(url, data)  # 发送请求同时传data表单  
response = urllib2.urlopen(req)  #接受反馈的信息  
the_page = response.read()  #读取反馈的内容  
print the_page