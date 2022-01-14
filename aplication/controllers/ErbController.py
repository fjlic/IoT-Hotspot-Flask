from flask import render_template, redirect, url_for, request, abort
from aplication.models.ErbModel import ErbModel

def index():
    erbs = ErbModel.query.all()
    print(erbs)
    return render_template('index.html', title = "Module|Erb", temp = "Erb", erbs=erbs)

def store():
    return ''

def show(id):
    if request.method == 'POST':
        erb = ErbModel(id=request.form['id'])
        title = 'Module|Erb'
    return render_template('show.html', title=title, erb=erb)

def update(id):
    return id

def destroy(id):
    return id