from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.pie import Pie

@app.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    if not user_id:
        return redirect('/')

    user = User.get_one_by_id(user_id)
    pies = Pie.get_all_pies()

    if not user:
        return redirect('/logout')

    return render_template('dashboard.html', user=user, pies=pies)

@app.route('/all_pies')
def all_pies():
    user_id = session.get('user_id')
    if not user_id:
        return redirect('/')

    user = User.get_one_by_id(user_id)
    pies = Pie.get_all_pies()

    if not user:
        return redirect('/logout')
    return render_template('all_pies.html', user=user, pies=pies)

@app.post('/create_pie/new')
def create_pie_new():
    if 'user_id' not in session:
        return redirect('/')

    if not Pie.validate(request.form):
        return redirect('/dashboard')

    data = {
        'name' : request.form['name'],
        'filling' : request.form['filling'],
        'crust' : request.form['crust'],
        'user_id': session['user_id']
    }

    Pie.save(data)
    return redirect('/dashboard')

@app.route('/edit_pie/<int:id>')
def edit_pie(id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        user_id = session['user_id']
        user = User.get_one_by_id(user_id)
        
        data = {
            'id': id
        }
        pie = Pie.get_single_pie(data)
    return render_template('edit_pie.html', user =  user, pie = pie )

@app.post('/edit_pie/update/<int:id>')
def edit_pie_update(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Pie.validate(request.form, id):
        return redirect(f'/edit_pie/{id}')
    data = {
        'id' : id,
        'name' : request.form['name'],
        'filling' : request.form['filling'],
        'crust' : request.form['crust'],
    }

    Pie.update(data)
    return redirect('/dashboard')

@app.route('/view_pie/<int:id>')
def view_pie(id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        user_id = session['user_id']
        user = User.get_one_by_id(user_id)
        
        data = {
            'id': id
        }
        pie = Pie.get_single_pie(data)
    return render_template('view_pie.html', user =  user, pie = pie )

@app.route('/delete_pie/<int:id>')
def delete_pie(id):
    data = {'id' : id}
    Pie.delete(data)
    return redirect('/dashboard')