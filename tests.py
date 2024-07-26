import pytest
from app import app as flask_app
from book_routes import book_bp  # Ensure this import matches your actual blueprint import
from models import db, Book  # Ensure this import matches your actual model import

# Create the Flask application and configure the database
@pytest.fixture
def app():
    flask_app.config['TESTING'] = True

    with flask_app.app_context():
        db.create_all() # method is called to create the database tables before running the tests
        yield flask_app
        db.session.remove()
        db.drop_all() # is called to drop the tables after the tests are done.

@pytest.fixture
def client(app):
    return app.test_client()

def test_add_book(client):
    response = client.post('/books', json={
        'title': 'Test Book',
        'author': 'Cake',
        'pages': 123,
        'language': 'English'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Book added successfully'

    # Verify the book was added to the database
    with flask_app.app_context():
        book = Book.query.filter_by(title='Test Book').first()
        assert book is not None
        assert book.author == 'Cake'
        assert book.pages == 123
        assert book.language == 'English'


def test_delete_book(client):
    with flask_app.app_context():
        book = Book(title="Hello", author="John", pages=100, language="English")
        db.session.add(book)
        db.session.commit()
        book_id = book.id
    
    response = client.delete(f'books/{book_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Book deleted successfully'
    
    with flask_app.app_context():
        book = db.session.get(Book,book_id)
        assert book is None

def test_get_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Books fetched'
    assert isinstance(data['data'], list)