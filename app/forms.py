from flask_wtf import Form
from wtforms import TextField, BooleanField, SelectField
from wtforms.validators import Required
from models import Content

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class CreateTranslation(Form):
    name = TextField("name", validators=[Required()])
    path = TextField("Path to file", validators=[Required()])
    dt = TextField("Date and Time. Format: y/m/d-h:m:s", validators=[Required()])
    VoD = BooleanField('VoD', default = False)

class DeleteTranslation(Form):
    names = SelectField(choices=[])