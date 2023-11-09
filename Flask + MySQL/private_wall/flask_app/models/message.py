from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models import user


class Message:
    DB = 'privatewall'
    def __init__(self, data):
        self.id = data['id']
        self.message = data['message']
        self.message_sent = data['message_sent']
        self.message_received = data['message_received']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO message (message, message_sent, message_received, created_at, updated_at) VALUES (%(message)s,%(message_sent)s,%(message_received)s, NOW(), NOW());"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM message WHERE message.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results