from flask_wtf import Form
from wtforms import TextField, BooleanField
#验证器用来简单地检查相应域提交的数据是否是空
from wtforms.validators import Required

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)