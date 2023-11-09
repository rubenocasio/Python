from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template('new.html')


@app.post('/create/user')
def create():
    if not User.validate(request.form):
    # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    User.save(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    users = User.get_all()
    return render_template('success.html', users = users)

