from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route('/ninjas')
def ninja_form():
    ninjas = Ninja.get_all()
    dojos = Dojo.get_all()
    return render_template("new.html", ninjas=ninjas, dojos=dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojos_id' : request.form['dojo_location']
    }
    Ninja.save(data)
    return redirect('/dojos')
