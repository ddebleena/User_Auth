from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class SignUpForm(FlaskForm):
    username = StringField('Usename')
    password = PasswordField('Password')
    submit = SubmitField('Sign Up')
    