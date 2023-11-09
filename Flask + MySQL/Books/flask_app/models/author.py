from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    DB = "books"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.fav_books =  []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.DB).query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def save(cls, data):
        query ="INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results

    @classmethod
    def get_favorite_books(cls, data):
        query= "SELECT * FROM authors LEFT JOIN favorites ON favorites.authors_id = authors.id LEFT JOIN books ON favorites.books_id = books.id WHERE authors.id = %(id)s"
        results = connectToMySQL(cls.DB).query_db(query,data)
        if results:
            author = cls(results[0])
            for r in results:
                data = {
                    'id' : r['books.id'],
                    'title' : r['title'],
                    'num_of_pages': r['num_of_pages'],
                    'created_at' : r['books.created_at'],
                    'updated_at' : r['books.updated_at']
                }
                squish = book.Book(data)
                author.fav_books.append(squish)
            return author
    
    @classmethod
    def add_fav_books_and_authors_together(cls, data):
        query ="INSERT INTO favorites (books_id, authors_id) VALUES (%(books_id)s, %(authors_id)s);"
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results