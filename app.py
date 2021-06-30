from logging import debug
from flask import Flask , render_template , request
from textblob import TextBlob
from textblob import Word

app = Flask(__name__)

@app.route('/home')
def Welcome():
    return render_template('base.html')

@app.route('/meaning', methods = ['GET','POST'])
def predict():
    a = request.form.get('word')
   


    Meaning = Word(a).definitions

    return render_template('base.html' ,meaning_text = f"The Meaning of the  {a} is {Meaning}.")

app.run(host = "0.0.0.0",debug=True)