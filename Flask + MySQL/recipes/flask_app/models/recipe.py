from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Recipe:
    DB = "recipesdb"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.minutes = data['minutes']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, minutes, instructions, date_made, created_at, updated_at, user_id) VALUES (%(name)s,%(description)s,%(minutes)s,%(instructions)s,%(date_made)s, NOW(), NOW(), %(user_id)s);"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, minutes = %(minutes)s, instructions = %(instructions)s, date_made = %(date_made)s, updated_at = NOW() WHERE recipes.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def delete(cls, data):
        query= "DELETE FROM recipes WHERE id= %(id)s;"
        return connectToMySQL(cls.DB).query_db( query, data)

    @classmethod
    def get_all_recipes(cls) -> list:
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.DB).query_db(query)
        recipes = []
        for r in results:
            recipes.append(cls(r))
        return recipes

    @classmethod
    def get_one_by_id(cls, id):
        query  = "SELECT * FROM recipes WHERE id = %(id)s;"
        data = {'id' : id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_the_whole_shabang(cls):
        query= "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results=connectToMySQL(cls.DB).query_db(query)
        recipes = [] 
        if results:
            for r in results:
                recipe = cls(r)
                data = {
                    **r,
                    'id' : r['users.id'],
                    'created_at' : r['users.created_at'],
                    'updated_at' : r['users.updated_at']
                }
                posted = user.User(data)
                recipe.posted = posted
                recipes.append(recipe)
        return recipes

    @classmethod
    def get_single_recipe(cls, data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return None
        recipe_data = results[0]
        recipe = cls(recipe_data)
        user_data = {
            'id': recipe_data['users.id'],
            'first_name': recipe_data['first_name'],
            'last_name': recipe_data['last_name'],
            'email': recipe_data['email'],
            'password': recipe_data['password'],
            'created_at': recipe_data['users.created_at'],
            'updated_at': recipe_data['users.updated_at']
        }
        recipe.user = user.User(user_data)
        return recipe


    @staticmethod
    def validate(data):
        is_valid = True
        if (len(data['name']) < 3):
            flash('Name is required', 'create')
            is_valid = False
        if (len(data['description']) < 3 or len(data['description']) > 150):
            flash('Description is required', 'create')
            is_valid = False
        if 'minutes' not in data:
            flash('Make 1 choice on the radio buttons, please', 'create')
            is_valid = False
        if (len(data['instructions']) < 3 or len(data['instructions']) > 150):
            flash('Instruction field is required', 'create')
            is_valid = False
        if len(data['date_made']) != 10:
            flash('Try again', 'create')
            is_valid = False
        return is_valid