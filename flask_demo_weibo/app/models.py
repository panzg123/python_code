#encoding:utf-8
'''
Created on 2015年12月17日

@author: pan
'''
from app import db
from sqlalchemy.orm import backref
from hashlib import md5
ROLE_USER = 0
ROLE_ADMIN = 1

#辅助表，来记录关注者与被关注者
followers=db.Table('followers',
    db.Column('follower_id',db.Integer,db.ForeignKey('user.id')),
    db.Column('followed_id',db.Integer,db.ForeignKey('user.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    #定义一个多对多的关系
    followed = db.relationship('User', #连接User实例到其他User实例上
        secondary=followers,           #指明了这种关系的辅助表followers
        primaryjoin=(followers.c.follower_id==id),#条件
        secondaryjoin = (followers.c.followed_id == id),#条件
        backref =db.backref('followers', lazy = 'dynamic'),
        lazy = 'dynamic'
    )
    
    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)    
    #返回一个与用户相关的头像，需要传入头像的大小
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)
    
    #静态方法，让USER类选择一个唯一的名字返回给用户
    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname=nickname).first() is None:
            return nickname
        version=2
        while True:
            new_nickname=nickname+str(version)
            if User.query.filter_by(nickname=new_nickname).first() is None:
                break
            version+=1
        return new_nickname
    #添加关注者
    def follow(self,user):
        if not self.is_following(user):
            self.followed.append(user)
            return self
    #移除关注者
    def unfollow(self,user):
        if self.is_following(user):
            self.followed.remove(user)
            return self
    #判断是否关注
    def is_following(self,user):
        return self.followed.filter(followers.c.followed_id == user.id).count()>0
    
    #查询关注者的微博,先连接post与follwers表，然后过滤，最后排序，http://www.pythondoc.com/flask-mega-tutorial/followers.html
    def followed_posts(self):
        return Post.query.join(followers,(followers.c.followed_id == Post.user_id)).filter(followers.c.follower_id == self.id).order_by(Post.timestamp.desc())
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
    