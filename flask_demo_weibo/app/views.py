#encoding:utf-8
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import LoginForm,EditForm,PostForm
from models import User, ROLE_USER, ROLE_ADMIN,Post
from datetime import datetime
from config import POSTS_PER_PAGE
from emails import follower_notification

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user
    #更新用户访问时间
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()

#显示用户信息
@app.route('/user/<nickname>')
@app.route('/user/<nickname>/<int:page>')
@login_required
def user(nickname, page=1):
    #查询用户发的blog
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    #分页显示
    posts = user.posts.paginate(page, POSTS_PER_PAGE, False)
    return render_template('user.html',
                           user=user,
                           posts=posts)

@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>',methods=['GET','POST'])
@login_required
def index(page=1):
    form=PostForm()
    #处理post表单
    if  form.validate_on_submit():
        post=Post(body=form.post.data,timestamp=datetime.utcnow(),author=g.user)
        db.session.add(post)
        db.session.commit()
        flash('your post is now live')
        #重定向的作用：避免刷新而导致的重复插入blog
        return redirect(url_for('index'))
#     posts = [
#         { 
#             'author': { 'nickname': 'John' }, 
#             'body': 'Beautiful day in Portland!' 
#         },
#         { 
#             'author': { 'nickname': 'Susan' }, 
#             'body': 'The Avengers movie was so cool!' 
#         }
#     ]
    #从数据库中查询blog,分页显示，page表示起始页，POSTS_PER_PAGE表示每页显示blog数目
    posts=g.user.followed_posts().paginate(page,POSTS_PER_PAGE,False).items
    return render_template('index.html',
        title = 'Home',
        form=form,
        posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        print 'login success'
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        print 'validate_on_submit --> try_login'
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
    print 'login_render_template'
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
        #设置为自己关注自己
        db.session.add(user.follow(user))
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


#edit页面路由
@app.route('/edit',methods=['GET','POST'])
@login_required
def edit():
    form = EditForm(g.user.nickname)#传入用户昵称
    if form.validate_on_submit():
        g.user.nickname=form.nickname.data
        g.user.about_me=form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved')
        return redirect('edit.html')
    #信息验证未成功
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)

#定制的错误处理器，404
@app.errorhandler(404)
def not_found_error():
    return render_template('404.html'),404

#定制的错误处理器，500
@app.errorhandler(500)
def internal_error():
    return render_template('500.html'),500

#处理关注连接
@app.route('/follow/<nickname>')
@login_required
def follow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User %s not found.'% nickname)
        redirect(url_for('index'))
        
    if user==g.user:
        flash('you cannot follow yourself')
        redirect(url_for('user',nickname=nickname))
    u=g.user.follow(user)
    if u is None:
        flash('Cannot follow '+nickname+'.')
        return redirect(url_for('user',nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash('you are now following '+nickname+'.')
    #新粉丝，发送通知邮件
    follower_notification(user, g.user)
    return redirect(url_for('user',nickname=nickname))
        
#处理取消关注连接
@app.route('/unfollow/<nickname>')
@login_required
def unfollow(nickname):
    user=User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User %s not found' % nickname)
        return redirect(url_for('index'))
    if user == g.user:
        flash('you cannot unfollow yourself')
        return redirect(url_for('user',nickname=nickname))
    u = g.user.unfollow(user)
    if u is None:
        flash('you cannot unfollow %s'%nickname)
        return redirect(url_for('user',nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash('you have stopped following %s .' % nickname)
    return redirect(url_for('user',nickname=nickname))
    