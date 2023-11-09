from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.survey import Survey

@app.route('/')
def index():
    return render_template('index.html')

@app.post('/create')
def create_survey():
    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment']
    }
    if not Survey.validate_survey(data):
        return redirect('/')
    Survey.save(data)
    return redirect("/")
