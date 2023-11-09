from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

from flask_app import app
bcrypt = Bcrypt(app)

from flask_app.models.user import User
from flask_app.models.message import Message

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/dashboard')
def success():
    if 'user_id' in session:
        users = User.get_all()
        return render_template('dashboard.html', users = users)
    return redirect('/')

@app.post('/register/user')
def register():
    if not User.validate(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect("/dashboard")

@app.post('/login')
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

@app.post('/logout')
def logout_session():
    if 'user_id' in session:
        session.pop('user_id', None)
    return redirect('/')

@app.post('/message/user/<int:id>')
def message_post(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : id
    }
    Message.save(data)
    return redirect('/dashboard')

@app.post('/message/user/<int:id>')
def delete(id):
    Message.delete(id)
    return redirect('/dashboard')