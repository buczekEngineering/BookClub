from BookClub import db


class Book(db.Model):
    __tablename__ = 'all_books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    author = db.Column(db.String(40))
    genre = db.Column(db.String(30))
    comment = db.relationship("Comment", backref="book", lazy=True)


    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


    def json(self):
        return {
        "id": self.id,
        "title":  self.title,
        "author": self.author,
        "genre": self.genre
        }


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.ForeignKey("all_books.id"), nullable=False)
    comment = db.Column(db.String(300))
    book = db.relationship('Book',
                               back_populates="comment")

    def __init__(self, comment):
        self.comment = comment

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()