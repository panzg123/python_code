#encoding:utf-8
'''
Created on 2015年12月20日

@author: pan
'''

from flask_mail import Message
from app import mail,app
from threading import Thread
from flask import render_template
from config import ADMINS

#发送邮件的方法
def send_mail(subject,sender,recipients,text_body,html_body):
    msg=Message(subject,sender=sender,recipients=recipients)
    msg.body=text_body
    msg.html=html_body
    mail.send(msg)

#新的粉丝，发送通知邮件    
def follower_notification(followed,follower):
    send_mail("[microblog] %s is now following you!" % follower.nickname, 
              ADMINS[0], 
              [followed.email], 
              render_template("follower_mail.txt",user=followed,follower=follower),
              render_template("follower_email.html",user=followed,follower=follower))
#异步的邮件发送    
def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)