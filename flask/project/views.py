"""
    views.py
        - Views is used to mange all of our app routes
"""
import os
import datetime
import hashlib as hash

from flask import render_template, redirect, url_for, request
from project import app
from project import db_session
from project.models.tasks import Tasks
from project.forms.formsTask import TaskForm

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/home/<user>")
def home(user):
    return render_template("public/home.html", user=user)

@app.route("/sign-up", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        hp = hash.md5(password.encode())
        print("User: ", username, " signed up with email: ", email, " with password: ", password, "hashed password: ", hp.hexdigest())
        return redirect(url_for('home', user=username))
    else:
        return render_template("public/sign_up.html")

@app.route("/about")
def about():
    return "About"

@app.route("/viewTasks")
def view_tasks():
    return render_template("public/viewTasks.html")

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
        #db_session.add(task)
        #db_session.commit()
        return redirect(url_for('success'))
    return render_template('public/createTask.html', form=form)

@app.route("/success/")
def success():
    return "Task has been added to task list"
