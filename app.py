from flask import Flask
from models import db
# from flask_marshmallow import Marshmallow
from book_routes import book_bp

app = Flask(__name__)

# Set the database URI for PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1122@localhost:5432/bookstore_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# ma = Marshmallow(app)

app.register_blueprint(book_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
