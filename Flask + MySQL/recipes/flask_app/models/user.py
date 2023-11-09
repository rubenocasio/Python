from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import recipe
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = "recipesdb"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s, NOW(), NOW());"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def get_one_by_id(cls, id):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id' : id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        print(results)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @staticmethod
    def validate_registration(data):
        is_valid = True

        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters.", 'register')
            is_valid = False

        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters.", 'register')
            is_valid = False

        if len(data['email']) == 0:
            flash("Email is required.", 'register')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address.", 'register')
            is_valid = False
        else:
            existing_user = User.get_by_email({'email': data['email']})
            if existing_user:
                flash('Email is already registered.', 'register')
                is_valid = False

        if len(data['password']) < 8:
            flash("Password must be at least 8 characters.", 'register')
            is_valid = False

        if data['password'] != data['confirm_password']:
            flash("Passwords do not match.", 'register')
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True
        user_from_db = User.get_by_email({'email': data['email']})

        if not user_from_db:
            flash("Invalid Email/Password", 'login')
            return False

        if not bcrypt.check_password_hash(user_from_db.password, data['password']):
            flash("Invalid Email/Password", 'login')
            is_valid = False

        return is_valid

    # @staticmethod
    # def validate(user):
    #     is_valid= True
    #     if len(user['first_name']) < 1:
    #         flash("Please enter a First Name. You do know your last name, right.!?", 'register')
    #         is_valid = False
    #     if len(user['last_name']) < 1:
    #         flash("Please enter a Last Name. You do know your last name, right.!?", 'register')
    #         is_valid = False
    #     if len(user['email']) < 1:
    #         flash("Please enter an email correctly next time.", 'register')
    #         is_valid = False
    #     elif not EMAIL_REGEX.match(user['email']): 
    #         flash("Invalid email address fool!", 'register')
    #         is_valid = False
    #     else:
    #         data = {
    #             'email' : user['email']
    #         }
    #         potential_user = User.get_by_email(data)
    #         if potential_user:
    #             flash('Email already registered.', 'register')
    #             is_valid =False
    #     if len(user['password']) < 4:
    #         flash("Please create password. Password must be 4 characters", 'register')
    #         is_valid=False
    #     if user['password'] != user['confirm_password']:
    #         flash("Passwords do not match.", 'register')
    #         is_valid = False
    #     return is_valid