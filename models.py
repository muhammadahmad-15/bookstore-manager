from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(20), nullable=False)

    def __init__(self, title, author, pages, language):
        self.title = title
        self.author = author
        self.pages = pages
        self.language = language

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'pages': self.pages,
            'language': self.language
        }