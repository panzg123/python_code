#encoding:utf-8
'''
Created on

@author: pan
'''

from app import app
from flask.templating import render_template
from forms import LoginForm
from flask.helpers import flash
from flask import redirect
@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in P  ortland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()#实例化一个表单对象，传递给模板，然后渲染表单
    #验证表单数据，所有验证都通过，将返回TRUE
    if form.validate_on_submit():
        #flash 函数是一种快速的方式下呈现给用户的页面上显示一个消息
        flash('Login requested for OpenID=" ' + form.openid.data+' ", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])