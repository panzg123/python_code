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
    
    
    def __init__(self,original_nickname,*args,**kwargs):
        Form.__init__(self, *args,**kwargs)
        self.originla_nickname=original_nickname
        
    #验证修改框中的昵称是否有效
    def validate(self):
        if not Form.validate(self):
            return False
        #表单中的昵称没有被修改
        if self.nickname.data ==self.originla_nickname:
            return True
        #查询该昵称是否在数据库中存在
        user = User.query().filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('this nickname is already in user.Please choose another one')
            return False
        return True
        