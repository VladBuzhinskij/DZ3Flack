from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField  
from wtforms.validators import DataRequired,Email,Length,EqualTo

class RegistrationForm(FlaskForm):
    name= StringField('name',validators=[DataRequired()])
    name1= StringField('name1',validators=[DataRequired()])
    mail= StringField('mail',validators=[DataRequired(), Email()])
    password=PasswordField('password', validators=[DataRequired(), Length(min=8)])
    confirm_passworf=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])