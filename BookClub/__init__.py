from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from BookClub import routes
# one of the configurations key that flask is using
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:3004@localhost:5432/books'
# connect app to db
db = SQLAlchemy(app)