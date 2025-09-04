from flask import Flask
app = Flask(__name__)

import flaskr.main
import joblib
app.rf = joblib.load("playground_rf.pkl")


