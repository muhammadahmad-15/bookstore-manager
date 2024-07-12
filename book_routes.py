from flask import Blueprint, jsonify, request
from models import db, Book
from shared_services.response_types import error_response, success_response

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/books', methods=['POST'])
def add_book():
    try:
        data = request.get_json()
        db.session.add(Book(**data))
        db.session.commit()
        return success_response(status_code=200, message='Book added successfuly')
    except Exception as e:
        return error_response(status_code=400, error=str(e))

@book_bp.route('/books', methods = ['GET'])
def get_books():
    try:
        books = Book.query.all()
        book_list = []
        for book in books:
            book_list.append(book.to_dict())
        return success_response(
            status_code=200, 
            message="Books fetched", 
            data=book_list
        )
    except Exception as e:
        return error_response(status_code=400, error=str(e))
    
@book_bp.route('/books/<int:book_id>', methods = ['DELETE'])
def delete_book(book_id):
    try:
        book = Book.query.get(book_id)
        if not book:
            return error_response(status_code=404, error='Book not found!')
        db.session.delete(book)
        db.session.commit()
        return success_response(status_code=200, message='Book deleted successfully')
    except Exception as e:
        return error_response(status_code=400, error=str(e))