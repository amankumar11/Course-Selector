from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import redirect,request,abort
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
@app.route('/')
def fun():
    return render_template('index.html')

@app.route('/<course>')
def hello(course):
    return course

if __name__ == '__main__':
    app.run(debug=True)