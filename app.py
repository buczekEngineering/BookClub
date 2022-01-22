from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, select

app = Flask(__name__)
# one of the configurations key that flask is using
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:3004@localhost:5432/books'
# connect app to db
db = SQLAlchemy(app)

@app.route("/")
def health():
    return render_template("index.html")

@app.route("/add", methods=['POST'])
def add_book():
    comment = request.form.get("comment", None)
    title = request.form.get('title', None)
    author = request.form.get('author', None)
    genre = request.form.get("genre", None)

    if comment != None:
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


# todo 2: user can sort books by author
# todo 5: user can enter book title and get all comments from another db
# todo 6: leanr more db stuff and apply
# todo: user table so that we know how added the comments
# todo: user can log in and add comment


class Book(db.Model):
    __tablename__ = 'all_books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    author = db.Column(db.String(40))
    genre = db.Column(db.String(30))
    comment= db.relationship("Comment", back_populates="book")

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.ForeignKey("all_books.id"),nullable=False)
    comment = db.Column(db.String(300))
    book = db.relationship('Book',
                               back_populates="comment")

    def __init__(self, comment):
        self.comment=comment


if __name__ == "__main__":
    app.run(debug=True)