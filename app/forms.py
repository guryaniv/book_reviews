from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# user login form generated using wtforms
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])     # DataRequired() validates it's not empty
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])  # DataRequired() validates it's not empty
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email')
    submit = SubmitField('Sign Up')