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
from project.models.User import User
from project.models.List import List
from project.models.Task import Task
from project.forms.TaskForm import TaskForm
from project.forms.UserForm import UserForm

@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/home")
def home():
    list = db_session.query(List).all()
    tasks = db_session.query(Task).all()
    # tasks = Task.query.all()
    return render_template("public/home.html", list=list, tasks=tasks)


@app.route("/sign-up", methods=["POST", "GET"])
def signup():
    # TODO: Use B Crypt to safely store passwords
    form = UserForm(request.form)
    if not form.validate_on_submit():
        return render_template('public/sign_up.html', form=form)
    if request.method == "POST":
        user = User(
                username = form.username.data,
                email = form.email.data,
                password = form.password.data,
                date_joined = datetime.datetime.now()
                )
        username = form.username.data
        print(user)
        db_session.add(user)
        db_session.commit()
        return redirect(url_for('home', user=username))
    else:
        return render_template("public/sign_up.html")

@app.route("/about")
def about():
    return "About"


@app.route("/viewTasks")
def view_tasks():
    list = db_session.query(List).all()
    print(list)
    tasks = db_session.query(Task).all()
    form = TaskForm(request.form)
    return render_template("public/viewTasks.html", tasks=tasks, form=form)

#Modal Edit Task
@app.route('/update', methods = ['GET', 'POST'])
def update():
    form = TaskForm(request.form)
    if request.method == 'POST':
        task = db_session.query(Task).get(request.form.get('id'))
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
        task = Task(
                list = form.list.data,
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
    data = db_session.query(Task).get(id)
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
        task = Task(
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
