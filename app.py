from flask import Flask, render_template, url_for,redirect

from datetime import datetime
from flask import redirect,request,abort

import os

from  courseFinder import *
app = Flask(__name__)
@app.route('/')
def fun():
    return render_template('index.html')

@app.route('/redirect',methods=['POST'])

def algo():
	lang=request.form['lang']
	return redirect('/'+lang)

@app.route('/suggestion')
def method_name():
   return render_template('suggestionForm.html')





@app.route('/<course>')
def hello(course):


	# print(course)
	return render_template('result.html',array=function(course))
    

if __name__ == '__main__':
    app.run(debug=True)