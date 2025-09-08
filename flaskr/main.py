from flaskr import app
from flask import render_template, request
import joblib
import pandas as pd


@app.route('/')
def index():

    return render_template(
        'index.html'
        )

def _predict(data):
    if data["previous"].sum() == 0:
        predict0True = app.gbrf_0True.predict(data)
        return predict0True
    else: 
        predict0False = app.gbrf_0False.predict(data)
        return predict0False
    

@app.route('/goto_predict')
def goto_predict():
    return render_template(
        'predict.html'
        )


@app.route('/set_X', methods=["POST"])
def set_X():
    X = {
    "age": int(request.form['age']),
    "job": request.form['job'],
    "marital": request.form['marital'],
    "education": request.form['education'],
    "default": int(request.form['default']),
    "balance": int(request.form['balance']),
    "housing": int(request.form['housing']),
    "loan": int(request.form['loan']),
    "contact": request.form['contact'],
    "duration": int(request.form['duration']),
    "campaign": int(request.form['campaign']),
    "pdays": int(request.form['pdays']),
    "previous": int(request.form['previous']),
    "poutcome": request.form['poutcome']
    }

    df = pd.DataFrame([X])

    return render_template(
        'result.html',
        pred = _predict(df)[0])

