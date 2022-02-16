from flask_restful import Resource, reqparse
from models.book import BookModel
from models.comments import CommentModel

REQUIRED_FIELD = "This filed is required."

def find_id(title, author):
    id = BookModel.query.filter_by(title=title, author=author).first().id
    return id
def find_comment(title):
    results = BookModel.query.filter_by(title=title).all()
    comments = [result.comments for result in results]
    return comments

class Comment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help=REQUIRED_FIELD)
    parser.add_argument('author', type=str, required=True, help=REQUIRED_FIELD)
    parser.add_argument('comment', type=str, required=True, help=REQUIRED_FIELD)

    def post(self):
        data = Comment.parser.parse_args()
        if not BookModel.find_by_title(data["title"]):
            return {'message': f'The book {data["title"]} does not exists'}, 400

        book_id = find_id(data["title"],data["author"])
        new_comment = CommentModel(data["comment"], book_id)
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
            comments = find_comment(data["title"])
            return {"title": data["title"],
                    "comments": comments}
