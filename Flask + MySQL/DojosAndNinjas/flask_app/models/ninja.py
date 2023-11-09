from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB = "dojosninjasdb"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos_id = data['dojos_id']

    @classmethod
    def _query_db(cls, query, data=None):
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = cls._query_db(query)
        return [cls(ninja) for ninja in results]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojos_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojos_id)s);"
        return cls._query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
        ninja = cls._query_db(query, data)
        return cls(ninja[0]) if ninja else None

    @classmethod
    def get_my_ninjas(cls, data):
        query = "SELECT * FROM ninjas WHERE ninjas.dojos_id = %(id)s;"
        ninjas = cls._query_db(query, data)
        if not ninjas:
            return []
        return [cls(ninja) for ninja in ninjas]


    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, updated_at= NOW() WHERE id=%(id)s;"
        return cls._query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM ninjas WHERE id=%(id)s;"
        return cls._query_db(query, data)