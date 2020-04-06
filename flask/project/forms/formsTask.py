from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    status = BooleanField('Completed', default=False)
    assigned_to = StringField('Assign to', validators=[DataRequired()])
