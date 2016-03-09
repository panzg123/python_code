#encoding:utf-8
'''
Created on 2016-3-8

@author: pan
'''

import time
import unittest
from gevent.hub import sleep


QUIT=False
LIMIT=10000000

#检查登录cookie
def check_token(conn,token):
    return conn.hget('login:',token)
#更新cookie内容
def update_token(conn,token,user,item=None):
    timestamp = time.time()
    #登录用户，更新登录时间
    conn.hset('login:',token,user)
    conn.zadd('recent:',token,timestamp)
    if item:
        conn.zadd('viewed:'+token,item,timestamp)
        #只保留最近浏览的25个商品
        conn.zremrangebyrank('viewed:'+token,0,-26)
        

def clean_sessions(conn):
    while not QUIT:
        size = conn.zcard('recent:')
        if size<LIMIT:
            time.sleep(1)
            continue
        end_index = min(size-LIMIT,100)
        tokens = conn.zrange('recent:',0,end_index-1)
        #要删除的记录浏览商品的有序集合
        session_keys = []
        for token in tokens:
            session_keys.append('viewed:'+token)
        #批量删除
        conn.delete(*session_keys)
        conn.hdel('login:',*token)
        conn.zrem('login:',*token)