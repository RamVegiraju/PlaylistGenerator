from flask import Flask, request, jsonify, render_template, session, redirect, url_for, session
#from flask_wtf import FlaskForm
#from wtforms import TextField,SubmitField
#from wtforms.validators import NumberRange
import requests
import pandas as pd
import numpy as np
import pickle
import joblib
from functions import getPredictions


model_knn = pickle.load(open('recommenderModel','rb'))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/', methods = ['POST'])
def getvalue():
    artistUser = request.form['artists']
    genreUser = str(request.form['genre'])
    languageUser = str(request.form['language'])
    playlistSizeUser = int(request.form['playlistsize'])
    recommendations = getPredictions(genreUser, languageUser,artistUser, playlistSizeUser)
    return render_template('table.html',  tables=[recommendations.to_html(classes='data')], titles=recommendations.columns.values)

if __name__ =='__main__':
    app.run(debug=True)


