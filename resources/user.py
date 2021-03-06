import bcrypt
from flask_restful import Resource, reqparse

from models.user import UserModel

FIELD_REQUIRED = "This field is required"


def user_exists(username):
    if UserModel.find_by_username(username):
        return True
    else:
        return False


def encode_pw(password):
    return bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())


def is_valid_pw(username, password):
    hashed_pw = UserModel.find_by_username(username).password
    if bcrypt.hashpw(password.encode("utf8"), hashed_pw) == hashed_pw:
        return True
    else:
        return False


def generate_json(status_code, msg):
    return {
               'message': msg,
           }, status_code


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help=FIELD_REQUIRED)
    parser.add_argument("password", type=str, required=True, help=FIELD_REQUIRED)

    def post(self):
        data = UserRegister.parser.parse_args()

        if user_exists(data["username"]):
            msg = "The username already exists"
            return generate_json(400, msg)

        hashed_pw = encode_pw(password=data["password"])
        user = UserModel(data["username"], hashed_pw)
        user.save_to_db()
        msg = "Register successfully completed!"
        return generate_json(200, msg)


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help=FIELD_REQUIRED)
    parser.add_argument("password", type=str, required=True, help=FIELD_REQUIRED)

    def post(self):
        data = UserLogin.parser.parse_args()
        if not user_exists(data["username"]):
            msg = 'Invalid username'
            return generate_json(301, msg)

        if not is_valid_pw(data["username"], data["password"]):
            msg = "Invalid password"
            return generate_json(302, msg)

        return {'message': 'You are logged in.'}, 200
