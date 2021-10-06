from app import db

tags = db.Table('authors',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(200))
    title = db.Column(db.String(200), index=True)
    status = db.Column(db.String(200), index=True)

    def __str__(self):
        return f"<Book {self.id} {self.title}>"

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    books = db.Column(db.Text)

    bibliography = db.relationship('Book', secondary=tags, lazy='subquery',
        backref=db.backref('authors', lazy=True))
    def __str__(self):
        return f"<Author {self.id} {self.name} {self.surname}>"
