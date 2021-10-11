from app import db
from sqlalchemy import inspect
from app.base_model import BaseModel

authors_to_books = db.Table('authors',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)

class Book(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True)
    author = db.Column(db.String(200))
    status = db.Column(db.String(200))

    _default_fields = [
        "title",
        "author",
        "status",
    ]
    _hidden_fields = [
        "id",
    ]
    _readonly_fields = [
    ]

    def __str__(self):
        return f"<id:{self.id}, {self.title} - {self.author}, {self.status}>"

book = Book()

class Author(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    books = db.Column(db.Text)

    bibliography = db.relationship('Book', secondary=authors_to_books, lazy='subquery',
        backref=db.backref('authors', lazy=True))#to można zastąpić db.relationship w klasie book

    _default_fields = [
        "name",
        "books",
    ]
    _hidden_fields = [
        "id",
    ]
    _readonly_fields = [
    ]

    def __str__(self):
        return f"<Author {self.id}, {self.name}>"

author = Author()


