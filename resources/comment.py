from flask import jsonify
from flask_restful import Resource, reqparse
from models.book import BookModel
from models.comments import CommentModel
from resources.book import Book

REQUIRED_FIELD = "This filed is required."


class Comment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help=REQUIRED_FIELD)
    parser.add_argument('author', type=str, required=True, help=REQUIRED_FIELD)
    parser.add_argument('comment', type=str, required=True, help=REQUIRED_FIELD)

    @classmethod
    def find_comment(cls, title):
        results = BookModel.query.filter_by(title=title).all()
        comments = [result.comments for result in results]
        print(f"Comments -> {comments}")
        print(f"Jsonified comments: {jsonify(list(map(lambda x: x.json(), comments)))}")
        return jsonify(comments)

    def post(self):
        data = Comment.parser.parse_args()
        if not BookModel.find_by_title(data["title"]):
            return {'message': f'The book {data["title"]} does not exists'}, 400

        new_comment = CommentModel(data["comment"], data["title"])
        try:
            CommentModel.save_to_db(new_comment)
        except:
            return {"message": "An error occurred while inserting the comment."}, 500

        return new_comment.json(), 201

class CommentList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, required=True, help=REQUIRED_FIELD)

    def post(self):
        data = CommentList.parser.parse_args()
        if BookModel.query.filter_by(title=data["title"]):
            comments = Comment.find_comment(data["title"])
            return {"title": data["title"],
                    "comments": jsonify(comments)}
