# TODO Dockerise web app as well like mongo
# TODO Auth Mechanisame
# TODO TESTS Coverages

from flask import Flask
from flask_pymongo import PyMongo

from consts import *

app = Flask(__name__)

# mongo default port was already occupied
app.config['MONGO_DBNAME'] = DATABASE_NAME
app.config['MONGO_URI'] = 'mongodb://localhost:27018/' + DATABASE_NAME

mongo = PyMongo(app)
tabs = mongo.db.tabs
