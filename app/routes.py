from flask import Flask, request, render_template

import requests


from app import app


from forms import LoginForm

from app.forms imprt LoginForm







app = Flask(__name__)






@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/home')
def home():
    return '<h1>This is the home pagge</h1>'




@app.route('/user/<username>')
def username(username):
    # show the user profile for that user
    return f'Hello {username}!'





@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('forms.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return '<h1>LOGGGED IN</h1>'
    else:
        return render_template('forms.html')




@app.route('/students/')
def students():
    students_list = ['Gabe, 'Will']
    return render_template('students.html', students_list=students_list)








    HW----------




@app.route('/ergast', #see pic




