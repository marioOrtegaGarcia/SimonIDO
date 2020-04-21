from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, validators

# Form ORM
class UserForm(FlaskForm):
        username = StringField('Username', validators=[
            validators.Length(min=4, max=25),
            validators.DataRequired()
        ])
        email = StringField('Email', validators=[
            validators.Length(min=6, max=35),
            validators.DataRequired()
        ])
        password = PasswordField('New Password', [
            validators.DataRequired(),
            validators.EqualTo('confirm', message='Passwords must match')
        ])
        confirm = PasswordField('Repeat Password')
        accept_tos = BooleanField('I accept the TOS (not that they exists)', [validators.DataRequired()])
