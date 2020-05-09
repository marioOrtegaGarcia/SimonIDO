from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired

# Form ORM
class ListForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Subject', validators=[DataRequired()])
    submit = SubmitField('Submit')
