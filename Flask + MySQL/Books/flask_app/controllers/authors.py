from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/')
def index():
    authors = Author.get_all()
    return render_template('index.html', authors = authors)

@app.post('/author/new')
def new_author():
    data = { **request.form}
    Author.save(data)
    return redirect('/')

@app.route('/author/<int:id>')
def show_author(id):
    data = { 'id' : id }
    authors = Author.get_favorite_books(data)
    books = Book.get_all()
    return render_template('author.html', books = books, authors = authors)

@app.post('/favoriteAuthors/add/<int:authors_id>')
def add_fav_authors_and_books_together(authors_id):
    data = { 
        'authors_id' : authors_id,
        'books_id': request.form['book']
        }
    Book.add_fav_books_and_authors_together(data)
    return redirect(f'/author/{authors_id}')