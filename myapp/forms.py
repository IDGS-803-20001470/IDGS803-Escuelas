from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id= IntegerField('Id')
    nombre = StringField('nombre')
    apellidos = StringField('apellidos')
    email = EmailField('email')
    
    
class MaestrosForm(Form):
    id= IntegerField('Id')
    nombre = StringField('nombre')
    apellidos = StringField('apellidos')
    email = EmailField('email')
    materia = StringField('materia')