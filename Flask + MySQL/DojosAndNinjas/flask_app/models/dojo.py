from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    DB = "dojosninjasdb"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def _query_db(cls, query, data=None):
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = cls._query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return cls._query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        dojo = cls._query_db(query, data)
        return cls(dojo[0]) if dojo else None

    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name=%(name)s, updated_at=NOW() WHERE id=%(id)s;"
        return cls._query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM dojos WHERE id=%(id)s;"
        return cls._query_db(query, data)