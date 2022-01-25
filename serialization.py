from marshmallow import Schema, fields, INCLUDE, EXCLUDE

# Marshmallows is -> turning classes objects into dictionaries
# take properties of the class
# turn them into dictionaries -> keys : title, author, values - <strings
# it can validate the data -< and returning dictionary
class BookSchema(Schema):
    title = fields.Int(required=True)
    author = fields.Str(required=True)
    desc = fields.Str()

class Book123:
    def __init__(self, title, author, desc):
        self.title = title
        self.author = author
        self.desc = desc


new_book = Book123("Life 3.0", "Max Tegmark", "Book about life in the future with AI")
book_schema = BookSchema(unknown=INCLUDE)
# serialization
book_dict = book_schema.dump(new_book)
print(book_dict)


incoming_book_data = {
    "title": "Clean Code",
    "author": "Bob Marrtin",
    "desc": "a book about writing better code"
}
# deserialization
book = book_schema.load(incoming_book_data)
print(book)