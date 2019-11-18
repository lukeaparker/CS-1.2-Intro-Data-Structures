from dictogram import Dictogram
from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    word_list = ['one', 'fish', 'two', 'fish', 'blue', 'fish', 'red', 'fish']
    dic = Dictogram(word_list=word_list)
    sample = Dictogram.sample(dic)
    print(sample)
    return render_template('index.html', sample=sample)




 




