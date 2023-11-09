from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
from flask_app.models import book

class Book:
    DB = "books"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.fav_auths = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.DB).query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def save(cls, data):
        query ="INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results

    @classmethod
    def get_favorite_authors(cls, data):
        query= "SELECT * FROM books LEFT JOIN favorites ON favorites.books_id = books.id LEFT JOIN authors ON favorites.authors_id = authors.id WHERE books.id = %(id)s"
        results = connectToMySQL(cls.DB).query_db(query,data)
        if results:
            book = cls(results[0])
            for r in results:
                data = {
                    'id' : r['authors.id'],
                    'name' : r['name'],
                    'created_at' : r['authors.created_at'],
                    'updated_at' : r['authors.updated_at']
                }
                squish = author.Author(data)
                book.fav_auths.append(squish)
            return book
        
    @classmethod
    def add_fav_books_and_authors_together(cls, data):
        query ="INSERT INTO favorites (books_id, authors_id) VALUES (%(id)s, %(authors_id)s);"
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results