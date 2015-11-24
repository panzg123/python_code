# -*- coding: utf-8 -*-
'''
Created on 2015年11月24日

@author: pan
'''
import requests
r = requests.get('http://httpbin.org/get')
print r.text