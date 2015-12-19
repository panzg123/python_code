#encoding:utf-8
#激活跨站点请求伪造保护
CSRF_ENABLED = True
#用来建立加密令牌
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

import os
basedir=os.path.abspath(os.path.dirname(__file__))
#数据库文件的路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#REPO是文件夹，将SQLAlchemy-migrate数据文件存储在这里
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#通过email发送错误日志，下面配置email参数
MAIL_SERVER='localhost'
MAIL_PORT=25
MAIL_USERNAME=None
MAIL_PASSWORD=None

#administrator
ADMINS=['you@example.com']