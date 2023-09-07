from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['radio_option'] = request.form['radio_option']
    session['checkbox_options'] = request.form.getlist('checkbox_options')
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', session_data=session)

if __name__ == "__main__":
    app.run(debug=True)
