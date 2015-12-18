#encoding:utf-8
from flask_wtf import Form
from wtforms import TextField, BooleanField,StringField,TextAreaField
#验证器用来简单地检查相应域提交的数据是否是空
from wtforms.validators import Required,DataRequired,Length

#用户登录的表单
class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

#编辑用户信息的表单
class EditForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])