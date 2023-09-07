from flask import Flask, render_template, request, redirect, session, flash
import random

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    # Initialize session variables if not present
    # check if a key is already present in the dictionary.
    # #If the key is present, it returns the key's value.
    # #If the key is not present, it inserts the key with
    # #a provided default value and then returns that default value.
    session.setdefault("message", "")
    session.setdefault('number', random.randrange(1, 101))
    
    return render_template("index.html", message=session['message'])

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.form['number'])
    if user_guess == session['number']:
        session['message'] = "You win!"
    elif user_guess > session['number']:
        session['message'] = 'Too high, guess lower.'
    else:
        session['message'] = 'Too low, guess higher.'
    
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop("number", None)
    session.pop("message", None)
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
