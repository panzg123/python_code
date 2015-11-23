#encoding: utf-8
import re

#match方法尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(re.match('www', 'www.baidu.com').span())
print(re.match('com', 'www.baidu.com'))

#re.search 扫描整个字符串并返回第一个成功的匹配。
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
#而re.search匹配整个字符串，直到找到一个匹配。

#re.sub用于替换字符串中的匹配项
phone = "2004-959-559 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num
# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print "Phone Num : ", num
