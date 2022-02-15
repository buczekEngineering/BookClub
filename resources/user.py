from flask_restful import Resource, reqparse

class User(Resource):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
