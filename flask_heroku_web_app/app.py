from flask import Flask, jsonify, request
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/') 

def home():
    return "Hello, World!"

app.run(port = 5000)