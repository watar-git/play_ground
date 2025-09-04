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
    predict = app.rf.predict(data)
    return predict

@app.route('/goto_predict')
def goto_predict():
    return render_template(
        'predict.html'
        )

@app.route('/into_rf', methods=['POST'])
def into_rf():
    X = {
        "duration":request.form['duration'],
        "balance":request.form['balance'],
        "contact_unknown":request.form['contact_unknown'],
        "poutcome_success":request.form['poutcome_success'],
        "housing":request.form['housing'],
        "contact_cellular":request.form['contact_cellular'],
        "pdays":request.form['pdays'],
        "age":request.form['age']
        }
    data = pd.DataFrame([X])
    return render_template(
        'result.html',
        pred = _predict(data)
        )
    
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
