"""
    views.py
        - Views is used to mange all of our app routes
"""
import os
import datetime

from flask import render_template, redirect, url_for
from project import app
from project import db_session
from project.models.tasks import Tasks
from project.forms.formsTask import TaskForm

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return "About"

@app.route("/createTask", methods=["POST", "GET"])
def create_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Tasks(subject = form.subject.data,
                    description = form.description.data,
                    status = form.status.data,
                    assigned_to = form.status.data,
                    data_created = datetime.datetime.now()
                    )
        db_session.add(task)
        db_session.commit()
        return redirect(url_for('success'))
    return render_template('public/createTask.html', form=form)

@app.route("/success/")
def success():
    return "Task has been added to task list"
