from flask import render_template, redirect, url_for, request, abort
from aplication.models.UserModel import UserModel

def index():
    users = UserModel.query.all()
    print(users)
    return render_template('index.html', title = "Module|User", temp = "User", users=users)

def store():
    return ''

def show(id):
    if request.method == 'POST':
        user = UserModel(id=request.form['id'])
        title = 'Module|User'
    return render_template('show.html', title=title, users=user)

def update(id):
    return id

def destroy(id):
    return id