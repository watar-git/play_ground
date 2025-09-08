from flask import Flask
app = Flask(__name__)

import flaskr.main
import joblib
app.gbrf_0True = joblib.load("previous_notequal0.pkl")
app.gbrf_0False = joblib.load("previous_equal0.pkl")


