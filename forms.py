from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, InputRequired #https://wtforms.readthedocs.io/en/2.3.x/validators/
# from email_validator import validate_email, EmailNotValidError #https://github.com/JoshData/python-email-validator

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    # try:
    email = StringField('Email', validators=[InputRequired("Please enter your email address."), Email("This field requires a valid email address")])
    #     valid = validate_email(email)
    #     email = valid.email
    # except EmailNotValidError as e:
    #     print(str(e))
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match")]) #diff from video
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired("Please enter your email address."), Email("This field requires a valid email address")])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

