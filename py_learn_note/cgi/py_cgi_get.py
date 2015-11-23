#encoding:utf-8
#一个解析get url的简单例子
#URL: /cgi-bin/hello_get.py?first_name=ZARA&last_name=ALI
# CGI处理模块
import cgi, cgitb
# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 
# 获取数据
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s %s</h2>" % (first_name, last_name)
print "</body>"
print "</html>"

#参考--> http://www.runoob.com/python/python-cgi.html