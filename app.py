from flask import Flask, request, jsonify, render_template
from flaskext.markdown import Markdown
import requests
import pandas as pd
import numpy as np

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)


"""
@app.route('/', methods = ["GET","POST"]) 
def index():
    if request.method == "POST":
        input_text = request.form.get('url')
        print("This is a test right now.")
    return render_template("index.html")
"""