from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Pie:
    DB = "eyepiedb"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.filling = data['filling']
        self.crust = data['crust']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO pies (name, filling, crust, created_at, updated_at, users_id) VALUES (%(name)s,%(filling)s,%(crust)s, NOW(), NOW(), %(user_id)s);"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def update(cls, data):
        query = "UPDATE pies SET name = %(name)s, filling = %(filling)s, crust = %(crust)s, updated_at = NOW() WHERE pies.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def delete(cls, data):
        query= "DELETE FROM pies WHERE id= %(id)s;"
        return connectToMySQL(cls.DB).query_db( query, data)

    @classmethod
    def get_all_pies (cls) -> list:
        query = "SELECT pies.id, name, filling, crust, pies.created_at, pies.updated_at, users.id as users_id, first_name, last_name, email, password, users.created_at as created_at, users.updated_at as updated_at FROM pies JOIN users on users.id = pies.users_id;"
        results = connectToMySQL(cls.DB).query_db(query)
        pies = []
        for p in results:
            pi = cls(p)
            pi.user = user.User(
                    {
            "id" : p['user_id'],
            "first_name" : p['first_name'],
            "last_name" : p['last_name'],
            "email" : p['email'],
            "password" : p['password'],
            "created_at" : p['created_at'],
            "updated_at" : p['updated_at']
            }
            )
            pies.append(pi)
        return pies

    @classmethod
    def get_one_by_id(cls, id):
        query  = "SELECT pies.id as id, name, * FROM pies WHERE id = %(id)s;"
        data = {'id' : id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all_pies(cls):
        query= "SELECT * FROM pies JOIN users ON users.id = pies.users_id;"
        results=connectToMySQL(cls.DB).query_db(query)
        pies = [] 
        if results:
            for p in results:
                pie = cls(p)
                data = {
                    **p,
                    'id' : p['users.id'],
                    'created_at' : p['users.created_at'],
                    'updated_at' : p['users.updated_at']
                }
                posted = user.User(data)
                pie.posted = posted
                print(posted.id)
                print(pie.posted.id)
                pies.append(pie)
        return pies

    @classmethod
    def get_single_pie(cls, data):
        query = "SELECT * FROM pies JOIN users ON users.id = pies.users_id WHERE pies.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return None
        pie_data = results[0]
        pie = cls(pie_data)
        user_data = {
            'id': pie_data['users.id'],
            'first_name': pie_data['first_name'],
            'last_name': pie_data['last_name'],
            'email': pie_data['email'],
            'password': pie_data['password'],
            'created_at': pie_data['users.created_at'],
            'updated_at': pie_data['users.updated_at']
        }
        pie.user = user.User(user_data)
        return pie

    @classmethod
    def find_by_name(cls, name):
        query = "SELECT * FROM pies WHERE name = %(name)s;"
        data = {'name': name}
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            return cls(result[0])
        return None
    
    @staticmethod
    def validate(data, pie_id = None):
        is_valid = True
        if len(data['name']) < 2:
            flash('Name must be at least 2 characters long.', 'create')
            is_valid = False
        else:
            existing_pie = Pie.find_by_name(data['name'])
            if existing_pie and (pie_id is None or existing_pie.id != pie_id):
                flash('Name already exists. Please choose a different name.', 'create')
                is_valid = False
        if len(data['filling']) < 2 or len(data['filling']) > 25:
            flash('Filling must be between 2 and 25 characters long.', 'create')
            is_valid = False
        if len(data['crust']) < 3:
            flash('Crust is required.', 'create')
            is_valid = False

        return is_valid