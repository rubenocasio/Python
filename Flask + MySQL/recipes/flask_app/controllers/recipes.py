from flask import render_template, redirect, request, session, flash

from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/dashboard')
def success():
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.get_one_by_id(user_id)
        recipes = Recipe.get_the_whole_shabang()
        return render_template('dashboard.html', user=user, recipes=recipes)
    return redirect('/')

@app.route('/create_recipe')
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('create_recipe.html')

@app.post('/create_recipe/new')
def create_recipe_new():
    if 'user_id' not in session:
        return redirect('/')

    if not Recipe.validate(request.form):
        return redirect('/create_recipe')

    data = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'minutes' : request.form['minutes'],
        'instructions' : request.form['instructions'],
        'date_made' : request.form['date_made'],
        'user_id': session['user_id']
    }

    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/view_recipe/<int:id>')
def view_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        user_id = session['user_id']
        user = User.get_one_by_id(user_id)
        
        data = {
            'id': id
        }
        recipe = Recipe.get_single_recipe(data)
    return render_template('view_recipe.html', user =  user, recipe = recipe )


@app.route('/edit_recipe/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        user_id = session['user_id']
        user = User.get_one_by_id(user_id)
        
        data = {
            'id': id
        }
        recipe = Recipe.get_single_recipe(data)
    return render_template('edit_recipe.html', user =  user, recipe = recipe )

@app.post('/edit_recipe/update/<int:id>')
def update_recipe(id):
    if 'user_id' not in session:
        return redirect('/')

    if not Recipe.validate(request.form):
        return redirect(f'/edit_recipe/{id}')
    data = {
        'id' : id,
        'name' : request.form['name'],
        'description' : request.form['description'],
        'minutes' : request.form['minutes'],
        'instructions' : request.form['instructions'],
        'date_made' : request.form['date_made'],
    }

    Recipe.update(data)
    return redirect('/dashboard')


@app.route('/delete_recipe/<int:id>')
def delete_recipe(id):
    data = {'id' : id}
    Recipe.delete(data)
    return redirect('/dashboard')