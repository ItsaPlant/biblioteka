from app import db
from sqlalchemy import inspect

authors_to_books = db.Table('authors',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)

class Book(db.Model):
    def __init__(self):
        pass 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True)
    author = db.Column(db.String(200))
    status = db.Column(db.String(200))

    def _dict(obj):
        dict_list = []
        for o in obj:
            dict_list.append(
                {c.key: getattr(o, c.key)
            for c in inspect(o).mapper.column_attrs}
            )
        return dict_list

    def __str__(self):
        return f"<id:{self.id}, {self.title} - {self.author}, {self.status}>"

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    books = db.Column(db.Text)

    bibliography = db.relationship('Book', secondary=authors_to_books, lazy='subquery',
        backref=db.backref('authors', lazy=True))#to można zastąpić db.relationship w klasie book

    def _dict(obj):
        return {c.key: getattr(obj, c.key)
                for c in inspect(obj).mapper.column_attrs}

    def _dict(obj):
        dict_list = []
        for o in obj:
            dict_list.append(
                {c.key: getattr(o, c.key)
            for c in inspect(o).mapper.column_attrs}
            )
        return dict_list

    def __str__(self):
        return f"<Author {self.id}, {self.name}>"


