from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from resources.book import Book, BooksList
from resources.user import UserRegister, UserLogin, User
from resources.comment import Comment, CommentList
from db import db

db_name = "data.db"
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "secret-key"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_name}"
app.config["PROPAGATE_EXCEPTION"] = True # enables to see the errors from flask
# app.config['SQLALCHEMY_DATABASE_URI']=f'postgresql://postgres:3004@localhost:5432/{db_name}'
api = Api(app)

jwt = JWTManager(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Book, "/book")
api.add_resource(BooksList, "/books")
api.add_resource(UserRegister, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(Comment, "/add_comment")
api.add_resource(CommentList, "/comments")
api.add_resource(User, "/user/<int:user_id>")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
