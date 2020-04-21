from flask_wtf import FlaskForm
from wtforms import TextField, StringField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import Length, Email, Required, DataRequired

# Form ORM
class TaskForm(FlaskForm):
        subject = StringField('Subject', validators=[DataRequired()])
        description = StringField('Description', validators=[DataRequired()])
        status = BooleanField('Completed', default=False)
        assigned_to = StringField('Assign to', validators=[DataRequired()])
        submit = SubmitField('Submit')