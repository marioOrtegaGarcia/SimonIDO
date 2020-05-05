"""
    views.py
        - Views is used to mange all of our app routes
"""
import os
import datetime
import hashlib as hash

from flask import render_template, redirect, url_for, request, flash
from sqlalchemy.orm import sessionmaker
from project import app
from project import db_session
from project.models.Tasks import Tasks
from project.models.Users import Users
from project.forms.TaskForm import TaskForm
from project.forms.UserForm import UserForm

@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/home")
def home():
    tasks = db_session.query(Tasks).all()
    # tasks = Tasks.query.all()
    return render_template("public/home.html", tasks=tasks)


@app.route("/sign-up", methods=["POST", "GET"])
def signup():
    # TODO: Use BCrypt to safely store passwords
    form = UserForm(request.form)
    if not form.validate_on_submit():
        return render_template('public/sign_up.html', form=form)
    if request.method == "POST":
        user = Users(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data,
            date_joined = datetime.datetime.now()
        )
        username = form.username.data
        print(user)
        db_session.add(user)
        db_session.commit()
        #username = request.form["username"]
        #email = request.form["email"]
        #password = request.form["password"]
        #hp = hash.md5(password.encode())
        #print("User: ", username, " signed up with email: ", email,
        #      " with password: ", password, "hashed password: ", hp.hexdigest())
        return redirect(url_for('home', user=username))
    else:
        return render_template("public/sign_up.html")

@app.route("/about")
def about():
    return "About"


@app.route("/viewTasks")
def view_tasks():
    tasks = db_session.query(Tasks).all()
    form = TaskForm(request.form)
    return render_template("public/viewTasks.html", tasks=tasks, form=form)

#Modal Edit Task
@app.route('/update', methods = ['GET', 'POST'])
def update():
    form = TaskForm(request.form)
    if request.method == 'POST':
        task = db_session.query(Tasks).get(request.form.get('id'))
        task.subject = form.subject.data
        task.description = form.description.data
        task.assigned_to = form.assigned_to.data
        task.status = form.status.data
        print(task)
        db_session.add(task)
        db_session.commit()
        flash("Task Updated Successfully")
        return redirect(url_for('view_tasks'))

#Modal View Insert
@app.route('/insert', methods = ['POST'])
def insert():
    form = TaskForm(request.form)
    if request.method == 'POST':
        task = Tasks(
            subject = form.subject.data,
            description = form.description.data,
            assigned_to = form.assigned_to.data,
            status = form.status.data,
            date_created = datetime.datetime.now()
            )
        print(task)
        db_session.add(task)
        db_session.commit()
        flash("Task Inserted Successfully")
        return redirect(url_for('view_tasks'))

#Delete task
@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    data = db_session.query(Tasks).get(id)
    db_session.delete(data)
    db_session.commit()
    flash("Task Deleted Successfully")
    return redirect(url_for('view_tasks'))


@app.route('/createTask', methods=['GET', 'POST'])
def createTask():
    form = TaskForm(request.form)
    if not form.validate_on_submit():
        return render_template('public/createTask.html', form=form)
    if request.method == 'POST':
        task = Tasks(
            subject = form.subject.data,
            description = form.description.data,
            assigned_to = form.assigned_to.data,
            status = form.status.data,
            date_created = datetime.datetime.now()
            )
        print(task)
        db_session.add(task)
        db_session.commit()
        return redirect(url_for('createTask'))


@app.route("/success/")
def success():
    return "Task has been added to task list"
