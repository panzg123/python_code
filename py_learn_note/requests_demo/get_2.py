# -*- coding: utf-8 -*-
'''
Created on 2015年11月24日

@author: pan
'''
import requests
payload = {'a':'杨','b':'hello'}
r = requests.post("http://httpbin.org/post", data=payload)
print r.text