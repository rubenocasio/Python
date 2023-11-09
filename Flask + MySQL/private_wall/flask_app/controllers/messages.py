from flask import render_template, redirect, request, session, flash
from flask_app import app

from flask_app.models.user import User
from flask_app.models.message import Message


@app.post('/message/user/<int:id>')
def message_post():
    if 'user_id' not in session:
        return redirect('/')
    Message.save(request.form)
    return redirect('/dashboard')

@app.post('/message/user/<int:id>')
def delete(id):
    Message.delete(id)
    return redirect('/dashboard')