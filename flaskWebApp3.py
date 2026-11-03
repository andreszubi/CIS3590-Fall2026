from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

#TODO: 10 read the cars.csv file and convert it to a pandas dataframe.
# 2) Create a route to return the first 10 row of the dataframe
# 3) Create a route to return the list of car manufacturers
# 4) Create a route to return the car name and price.

df = pd.read_csv('cars.csv')

app.route('/')
def index()