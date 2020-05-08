from flask_wtf import FlaskForm
from wtforms import TextField, StringField, BooleanField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import Length, Email, Required, DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from project import db_session
from project.models.List import List

# Form ORM
class TaskForm(FlaskForm):
        id = HiddenField('id')
        subject = StringField('Subject', validators=[DataRequired()])
        description = StringField('Description', validators=[DataRequired()])
        status = BooleanField('Completed', default=False)
        assigned_to = StringField('Assign to', validators=[DataRequired()])
        list = QuerySelectField(query_factory=lambda: db_session.query(List).all())
        submit = SubmitField('Submit')
