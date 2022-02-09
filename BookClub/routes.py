from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from BookClub import app
from BookClub import db
from BookClub.models import Comment, Book


@app.route("/")
def health():
    return render_template("templates/index.html")

@app.route("/add", methods=['POST'])
def add_book():
    comment = request.form.get("comment", None)
    title = request.form.get('title', None)
    author = request.form.get('author', None)
    genre = request.form.get("genre", None)

    if comment:
        new_book = Book(title, author, genre)
        new_book.comment = [Comment(comment=comment)]
        db.session.add(new_book)
        db.session.commit()
    else:
        new_book = Book(title, author, genre)
        db.session.add(new_book)
        db.session.commit()

    return render_template("success.html", title=title, author=author)

@app.route("/find_by_id", methods=["POST"])
def find_by_genre():
    genre = request.form.get('genre')
    books = Book.query.filter_by(genre=genre).all()
    return render_template("display_all_books.html", genre=genre, books=books)

@app.route("/go_back", methods=["POST"])
def go_back():
    return render_template("index.html")

@app.route("/display_comments", methods=["POST"])
def get_review():
    title = request.form.get("title")
    query = select([Comment.comment]).where(Book.title == title)
    comments = db.session.execute(query)
    return render_template("display_comments.html", title=title, comments=comments)