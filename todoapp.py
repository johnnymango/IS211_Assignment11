#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 11.  To Do App"""


#Modules
from flask import Flask, render_template, request, redirect, flash
import re

#App configuration
app = Flask(__name__)
todolist = []

#Home Page
@app.route('/')
def todoapp():
    return render_template('index.html', todolist=todolist)

#Submit function
@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    error = None
    task1 = request.form['task1']
    email1 = request.form["email1"]
    priority1 = request.form["priority1"]
    task2 = request.form['task2']
    email2 = request.form["email2"]
    priority2 = request.form["priority2"]
    task3 = request.form['task3']
    email3 = request.form["email3"]
    priority3 = request.form["priority3"]

    todolist.append(task1)

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email1):
        error = "Invalid Email"
        return redirect('/')

    else:
        todolist.append(task1)
        return render_template('index.html', priority1=priority1, email1=email1, task1=task1,
                                task2=task2, email2=email2, priority2=priority2,
                                task3=task3, email3=email3, priority3=priority3,
                                todolist=todolist, error=error)

#Clear Function
@app.route('/clear', methods = ['POST'])
def clear():
    todolist = []
    return render_template('index.html', todolist=todolist)


if __name__ == "__main__":
    app.run()
