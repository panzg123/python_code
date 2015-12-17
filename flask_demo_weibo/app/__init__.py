#encoding:utf-8
'''
Created on 

@author: pan
'''
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')#读取配置文件
from app import views
