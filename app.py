import codecs

import flask
from flask import Flask, render_template,request
#import pyodbc
import csv


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/dashboard')
def tableaudashboard():
    return render_template("tableau.html")

@app.route('/register')
def register():
    return render_template("register.html")


    #return render_template('homepage.html')

app.run()
