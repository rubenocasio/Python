pip install pipenv
pipenv install flask

python -m pipenv <command to use> ## Only if errors out

pipenv shell

pip list ## List of Pip commands

app.run(debug=True, host="localhost", port=8000) ## Changing port to 8000

create server.py file
Starter contents:

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__=="__main__":
    app.run(debug=True)

python server.py


