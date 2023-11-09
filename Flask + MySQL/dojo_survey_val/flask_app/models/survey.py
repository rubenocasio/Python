from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Survey:
    DB = "surveys"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM surveys;"
        data = {'id': data}
        results = connectToMySQL(cls.DB).query_db(query, data)
        if results:
            return cls(results[0])
        return None
    
    @classmethod
    def save(cls, data):
        query ="INSERT INTO survey (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @staticmethod
    def validate_survey(survey):
        is_valid = True # we assume this is true

        if len(survey['name']) < 5:
            flash("Name must be at least 5 characters.")
            is_valid = False

        if len(survey['location']) < 5:
            flash("location must be at least 5 characters.")
            is_valid = False

        if len(survey['language']) < 2:
            flash("language must be 2 or greater.")
            is_valid = False

        if len(survey['comment']) < 10:
            flash("comment must be at least 10 characters.")
            is_valid = False

        return is_valid

