#encoding:utf-8
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, ValidationError
from wtforms.fields.simple import TextAreaField
from wtforms.fields.core import BooleanField, SelectField
from ..models import Role,User


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

class EditProfileForm(Form):
    name=StringField('Real name',validators=[Length(0,64)])
    location=StringField('Location',validators=[Length(0,64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')
    
class EditProfileAdminForm(Form):
    #验证电子邮箱
    email=StringField('Email',validators=[Required(),Length(1,64),Email()])
    username=StringField('Username',validators=[
        Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
                                'Username must have only letters,')])
    confirmed=BooleanField('Confirmed')
    role=SelectField('Role',coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')
    
    def __init__(self,user,*args,**kwargs):
        super(EditProfileAdminForm,self).__init__(*args,**kwargs)
        self.role.choices=[(role.id,role.name)
                           for role in Role.query.order_by(Role.name).all()]
        self.user=user
    #判断email地址是否改变或者数据库中是否已经存在该email
    def validate_email(self,field):
        if field.data != self.user.email and \
            User.query.filter_by(emial=field.data).first():
            raise ValidationError('Email already regestered')
    #判断username是否改变或者数据库中该username是否存在    
    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
