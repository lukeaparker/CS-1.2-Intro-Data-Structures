import os 
import sample
import histogram
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId


host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Playlister')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
tweet = db.tweet

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html', tweet=tweet.find())

@app.route('/')
def input_word():
    """Submit a new word."""
    get = sample.get_word(histogram)
    word = ""
    print(word)
    return get

 




