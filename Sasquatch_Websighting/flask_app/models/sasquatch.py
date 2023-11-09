from datetime import datetime
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Sasquatch:
    DB = "sasquatchdb"
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.sighting_date = data['sighting_date']
        self.num_of_sas = data['num_of_sas']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO sightings (location, sighting_date, num_of_sas, description, created_at, updated_at, user_id) VALUES (%(location)s,%(sighting_date)s,%(num_of_sas)s,%(description)s, NOW(), NOW(), %(user_id)s);"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def update(cls, data):
        query = "UPDATE sightings SET location = %(location)s, sighting_date = %(sighting_date)s, num_of_sas = %(num_of_sas)s, description = %(description)s, updated_at = NOW() WHERE sasquatchs.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def delete(cls, data):
        query= "DELETE FROM sightings WHERE id= %(id)s;"
        return connectToMySQL(cls.DB).query_db( query, data)

    @classmethod
    def get_all_sasquatchs(cls) -> list:
        query = "SELECT sightings.id, location, description, sighting_date, num_of_sas, sightings.created_at, sightings.updated_at, users.id as user_id, first_name, last_name, email, password, users.created_at as created_at, users.updated_at as updated_at FROM sightings JOIN users on users.id = sightings.user_id;"
        results = connectToMySQL(cls.DB).query_db(query)
        sightings = []
        for s in results:
            sight = cls(s)
            sight.user = user.User(
                    {
            "id" : s['user_id'],
            "first_name" : s['first_name'],
            "last_name" : s['last_name'],
            "email" : s['email'],
            "password" : s['password'],
            "created_at" : s['created_at'],
            "updated_at" : s['updated_at']
            }
            )
            sightings.append(sight)
        return sightings

    @classmethod
    def get_one_by_id(cls, id):
        query  = "SELECT sightings.id as id, location, * FROM sightings WHERE id = %(id)s;"
        data = {'id' : id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_the_whole_shabang(cls):
        query= "SELECT * FROM sightings JOIN users ON users.id = sightings.user_id;"
        results=connectToMySQL(cls.DB).query_db(query)
        sasquatchs = [] 
        if results:
            for r in results:
                sasquatch = cls(r)
                data = {
                    **r,
                    'id' : r['users.id'],
                    'created_at' : r['users.created_at'],
                    'updated_at' : r['users.updated_at']
                }
                posted = user.User(data)
                sasquatch.posted = posted
                sasquatchs.append(sasquatch)
        return sasquatchs

    @classmethod
    def get_single_sasquatch(cls, data):
        query = "SELECT * FROM sightings JOIN users ON users.id = sightings.user_id WHERE sightings.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return None
        sasquatch_data = results[0]
        sasquatch = cls(sasquatch_data)
        user_data = {
            'id': sasquatch_data['users.id'],
            'first_name': sasquatch_data['first_name'],
            'last_name': sasquatch_data['last_name'],
            'email': sasquatch_data['email'],
            'password': sasquatch_data['password'],
            'created_at': sasquatch_data['users.created_at'],
            'updated_at': sasquatch_data['users.updated_at']
        }
        sasquatch.user = user.User(user_data)
        return sasquatch


    @staticmethod
    def validate(data):
        is_valid = True
        if (len(data['location']) < 3):
            flash('Location is required', 'create')
            is_valid = False
        if (len(data['description']) < 3 or len(data['description']) > 50):
            flash('Description is required', 'create')
            is_valid = False
        if (len(data['num_of_sas']) < 1):
            flash('Instruction field is required', 'create')
            is_valid = False
        if len(data['sighting_date']) != 10:
            flash('Try again. Date must be in the format YYYY-MM-DD.', 'create')
            is_valid = False
        else:
            try:
                sighting_date = datetime.strptime(data['sighting_date'], '%Y-%m-%d').date()
                if sighting_date >= datetime.now().date():
                    flash('Sighting date must be in the past.', 'create')
                    is_valid = False
            except ValueError:
                flash('Invalid date format. Please use YYYY-MM-DD.', 'create')
                is_valid = False
        return is_valid