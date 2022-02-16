from flask_restful import Resource, reqparse
from models.book import BookModel
from models.comments import CommentModel

REQUIRED_FIELD = "This filed is required."

def find_id(title, author):
    id = BookModel.query.filter_by(title=title, author=author).first().id
    return id

class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help=REQUIRED_FIELD)
    parser.add_argument('author', type=str, required=True, help=REQUIRED_FIELD)
    parser.add_argument('comment', type=str)

    def get(self):
        data = Book.parser.parse_args()
        book = BookModel.find_by_title(data["title"])
        if book:
            return book.json()
        return {"message": "book not found"}, 404

    def post(self):
        data = Book.parser.parse_args()
        if BookModel.find_by_title(data["title"]):
            return {'message': f'A book with the name {data["title"]} already exists'}, 400
        new_book = BookModel(data["title"], data["author"])
        try:
            BookModel.save_to_db(new_book)
        except:
            return {"message": "An error occurred while inserting the book."}, 500

        return new_book.json(), 201

    def delete(self):
        data = Book.parser.parse_args()
        book = BookModel.find_by_title(data["title"])
        if book:
            book.delete_from_db()

        return {"message": "Item deleted"}

    def put(self):
        data = Book.parser.parse_args()
        book = BookModel.find_by_title(data["title"])
        if book is None:
            book = BookModel(data["title"], data["author"])
            book.save_to_db()
        else:
            book.author = data["author"]

        book.save_to_db()

        return book.json()


class BooksList(Resource):

    def get(self):
        return {"books": list(map(lambda x: x.json(), BookModel.query.all()))}
