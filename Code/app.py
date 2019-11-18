from dictogram import Dictogram
from markov import Markov
from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    word_list = ['one', 'fish', 'two', 'fish', 'blue', 'fish', 'red', 'fish']
    sentence = Markov(word_list=word_list)
    samseple = sentence.sample_markov()
    print(sample)
    return render_template('index.html', sample=sample)




 




