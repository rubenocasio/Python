from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route('/')
def root_redirect():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route("/dojos/<int:dojos_id>" ,methods=['POST'])
def detail_page(dojos_id):
    data = {'id': dojos_id}
    dojo = Dojo.get_one(data)
    ninja = Ninja.get_my_ninjas(data)
    return render_template("dojos.html", dojo=dojo, ninja = ninja)
