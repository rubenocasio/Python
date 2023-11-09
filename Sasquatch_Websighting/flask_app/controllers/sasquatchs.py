from flask import render_template, redirect, request, session
from datetime import datetime

from flask_app import app
from flask_app.models.user import User
from flask_app.models.sasquatch import Sasquatch

@app.route('/dashboard')
def success():
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.get_one_by_id(user_id)
        sasquatchs = Sasquatch.get_all_sasquatchs()
        print(user.id)
        return render_template('dashboard.html', user=user, sasquatchs = sasquatchs)
    return redirect('/')

@app.route('/create_sasquatch')
def create_sasquatch():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('create_sasquatch.html')

@app.post('/create_sasquatch/new')
def create_sasquatch_new():
    if 'user_id' not in session:
        return redirect('/')

    if not Sasquatch.validate(request.form):
        return redirect('/create_sasquatch')

    data = {
        'location' : request.form['location'],
        'sighting_date' : request.form['sighting_date'],
        'num_of_sas' : request.form['num_of_sas'],
        'description' : request.form['description'],
        'user_id': session['user_id']
    }

    Sasquatch.save(data)
    return redirect('/dashboard')

@app.route('/view_sasquatch/<int:id>')
def view_sasquatch(id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        user_id = session['user_id']
        user = User.get_one_by_id(user_id)
        
        data = {
            'id': id
        }
        sasquatch = Sasquatch.get_single_sasquatch(data)
    return render_template('view_sasquatch.html', user =  user, sasquatch = sasquatch )


@app.route('/edit_sasquatch/<int:id>')
def edit_sasquatch(id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        user_id = session['user_id']
        user = User.get_one_by_id(user_id)
        
        data = {
            'id': id
        }
        sasquatch = Sasquatch.get_single_sasquatch(data)
    return render_template('edit_sasquatch.html', user =  user, sasquatch = sasquatch )

@app.post('/edit_sasquatch/update/<int:id>')
def update_sasquatch(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Sasquatch.validate(request.form):
        return redirect(f'/edit_sasquatch/{id}')
    data = {
        'id' : id,
        'location' : request.form['location'],
        'sighting_date' : request.form['sighting_date'],
        'num_of_sas' : request.form['num_of_sas'],
        'description' : request.form['description'],
    }

    Sasquatch.update(data)
    return redirect('/dashboard')


@app.route('/delete_sasquatch/<int:id>')
def delete_sasquatch(id):
    data = {'id' : id}
    Sasquatch.delete(data)
    return redirect('/dashboard')