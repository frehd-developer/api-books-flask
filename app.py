from flask import Flask, request, make_response, jsonify
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from database import db
from models import Book
import os


app = Flask(__name__)
enviroment_configuration = os.environ["CONFIGURATION_SETUP"]
app.config.from_object(enviroment_configuration)

db.init_app(app)
ma = Marshmallow(app)
api = Api(app)


class BookSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "year", "author")
        model = Book

book_schema = BookSchema()
books_schema = BookSchema(many=True)

class BookSimple(Resource):
    def get(self, id):
        book = Book.query.filter_by(id=id).first()
        if book is None:
            return {"message": "Book is not found"}, 404
        return book_schema.dump(book), 200

    def put(self, id):
        data = request.form
        book = Book.query.filter_by(id=id).first_or_404()
        book.title = data.get("title")
        book.year = data.get("year")
        book.author = data.get("author")
        db.session.commit()
        return book_schema.dump(book), 201
    
    def delete(self, id):
        book = Book.query.filter_by(id=id).first_or_404()
        db.session.delete(book)
        db.session.commit()
        return {"message": "Deleted successfully"}, 204


class BookList(Resource):
    def get(self):
        books = Book.query.all()
        return books_schema.dump(books), 200

    def post(self):
        data = request.form
        book = Book(
            title=data.get('title'),
            year=data.get('year'),
            author=data.get('author'),
        )
        try:
            db.session.add(book)
            db.session.commit()
        except Exception as e:
            return {"message": f"Error: {str(e)}"}
        return book_schema.dump(book), 201

api.add_resource(BookList, "/books")
api.add_resource(BookSimple, "/books/<string:id>")

if __name__ == '__main__':
    app.run()
    db.create_all()
