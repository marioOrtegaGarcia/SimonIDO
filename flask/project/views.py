"""
    views.py
        - Views is used to mange all of our app routes
"""
import os
import datetime
import hashlib as hash

from flask import render_template, redirect, url_for, request
from sqlalchemy.orm import sessionmaker
from project import app
from project import db_session
from project.models.User import User
from project.models.List import List
from project.models.Task import Task
from project.forms.TaskForm import TaskForm
from project.forms.UserForm import UserForm
from project.forms.ListForm import ListForm

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/home")
def home():
    list = db_session.query(List).all()
    list_form = ListForm(request.form)
    task_form = TaskForm(request.form)
    return render_template("public/home.html", list=list, list_form=list_form, task_form=task_form)

@app.route("/insert-list", methods = ['POST'])
def insert_list():
    form = ListForm(request.form)
    if request.method == 'POST':
        list = List(name = form.name.data)
        db_session.add(list)
        db_session.commit()
    return redirect(url_for('home'))

@app.route('/insert-task', methods = ['POST'])
def insert_task():
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
        return redirect(url_for('home'))

@app.route('/update-task', methods = ['GET', 'POST'])
def update_task():
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
        return redirect(url_for('home'))

@app.route('/delete/task-<id>/', methods=['GET', 'POST'])
def delete_task(id):
    data = db_session.query(Task).get(id)
    db_session.delete(data)
    db_session.commit()
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

@app.route("/view-tasks")
def view_tasks():
    list = db_session.query(List).all()
    print(list)
    tasks = db_session.query(Task).order_by(Task.date_created.asc())
    form = TaskForm(request.form)
    return render_template("public/viewTasks.html", tasks=tasks, form=form)

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
        db_session.add(user)
        db_session.commit()
        return redirect(url_for('home', user=username))
    else:
        return render_template("public/sign_up.html")

@app.route("/about")
def about():
    return "About"

@app.route("/success/")
def success():
    return "Task has been added to task list"
