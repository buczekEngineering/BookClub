from db import db


class CommentModel(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(1000))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    book = db.relationship('BookModel')
    # user = db.relationship('UserModel')

    def __init__(self, comment, book_id):
        self.comment = comment
        self.book_id = book_id
        # self.user_id = user_id

    def json(self):
        return {"comment": self.comment}

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

