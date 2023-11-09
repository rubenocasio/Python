from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/books')
def booooooks():
    books = Book.get_all()
    return render_template('books.html', books = books)

@app.post('/book/new')
def new_booooook():
    data = { **request.form}
    Book.save(data)
    return redirect('/books')

@app.route('/book/<int:id>')
def show_book(id):
    data = { 'id' : id }
    books = Book.get_favorite_authors(data)
    authors = Author.get_all()
    return render_template('book.html', books = books, authors = authors)

@app.post('/favoriteBooks/add/<int:id>')
def add_fav_books_and_authors_together(id):
    data = { 
        'id' : id,
        'authors_id': request.form['author']
        }
    Book.add_fav_books_and_authors_together(data)
    return redirect(f'/book/{id}')