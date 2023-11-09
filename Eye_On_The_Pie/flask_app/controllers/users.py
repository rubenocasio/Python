from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt

from flask_app import app
bcrypt = Bcrypt(app)

# from flask_app.models.pie import Pie
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.post('/register/user')
def register():
    if not User.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
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
    if not User.validate_login(request.form):
        return redirect('/')
    user_in_db = User.get_by_email({"email": request.form["email"]})
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

@app.route('/logout')
def logout_session():
    if 'user_id' in session:
        session.pop('user_id', None)
    return redirect('/')