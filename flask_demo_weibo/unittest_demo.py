#encoding:utf-8
'''
Created on 2015年12月19日

@author: pan
@attention: 用unittest来构建个简单的测试框架
'''

import os
import unittest

from config import basedir
from app import app,db
from app.models import User

#测试类，继承自unittest.TestCase
class TestCase(unittest.TestCase):
    #setUp建立测试环境
    def setUp(self):
        app.config['TESTING']=True
        app.config['WTF_CSRF_ENABLED']=False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app=app.test_client()
        db.create_all()
    #测试环境的建立    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    #测试avatar    
    def test_avatar(self):
        u = User(nickname='john',email='john@example.com')
        avatar=u.avatar(128)
        expected = 'http://gravatar.duoshuo.com/avatar/d4c74594d841139328695756648b6bd6'
        assert avatar[0:len(expected)] == expected
    #测试make_unique_nickname    
    def test_make_unique_nickname(self):
        u = User(nickname='john', email='john@example.com')
        db.session.add(u)
        db.session.commit()
        nickname = User.make_unique_nickname('john')
        assert nickname != 'john'
        u = User(nickname=nickname, email='susan@example.com')
        db.session.add(u)
        db.session.commit()
        nickname2 = User.make_unique_nickname('john')
        assert nickname2 != 'john'
        assert nickname2 != nickname

if __name__=='__main__':
    unittest.main()