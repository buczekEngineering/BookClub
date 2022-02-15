from flask import Flask
from flask_restful import  Api
from resources.book import Book, BooksList
from db import db

db_name= "data.db"
app = Flask(__name__)
#app.secret_key = "secret-key"
#app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
#app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite://{db_name}"
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:3004@localhost:5432/books_new'
api = Api(app)

api.add_resource(Book, "/book")
api.add_resource(BooksList, "/books")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
