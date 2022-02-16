import sqlite3
from db import db


class BookModel(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))

    comments = db.relationship('CommentModel', lazy='dynamic')

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def json(self):
        return {"title": self.title,
                "author": self.author,
                "comments": [comment.json() for comment in self.comments.all()]}

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

