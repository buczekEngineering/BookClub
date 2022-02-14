from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = "secret-key"
api = Api(app)

# api is using resources and every resource needs to be a class
books = []

class Book(Resource):
    def get(self, title):
        # next will give us the first item matched be the filter function
        book = next(filter(lambda x: x["title"] == title, books), None)
        return {"book": book}, 200 if book is not None else 404

    def post(self, title):
        # if we found the book
        if next(filter(lambda x: x["title"] == title, books), None) is not None:
            return {'message': f'A book with the name {title} already exists'}, 400
        # else append it to the list
        else:
            data = request.get_json()
            new_book = {"title": title, "author": data["author"]}
            books.append(new_book)
            return new_book, 201

class BooksList(Resource):
    def get(self):
        return {"books": books}


api.add_resource(Book, "/book/<string:title>")
api.add_resource(BooksList, "/books")
app.run(port=5000, debug=True)
