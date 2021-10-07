from app import db

authors_to_books = db.Table('authors',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True)
    author = db.Column(db.String(200))
    status = db.Column(db.String(200))

    def __str__(self):
        return f"id:{self.id}, {self.title} - {self.author}, {self.status}>"

    def get_books(self):
        data = Book.query.all()
        dict_list=[]
        for b in data:
            d={
            'id': b.id,
            'author': b.author,
            'title': b.title,
            'status': b.status
            }
            dict_list.append(d)
        return dict_list

    def get_book(self, title):
        data = Book.query.filter_by(title=title).first()
        data_dict = {
            'id': data.id,
            'author': data.author,
            'title': data.title,
            'status': data.status
        }
        return data_dict

    def post_book(self, author, title, status):
        u = Book(author=author, title=title, status=status)
        db.session.add(u)
        db.session.commit()

    def post_book_update(self, author, title, status):
        data = self.get_book(title)
        u = Book(author=author, title=title, ststus=status)
        db.session.delete(data)
        db.session.add(u)
        db.session.commit()

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    books = db.Column(db.Text)

    bibliography = db.relationship('Book', secondary=authors_to_books, lazy='subquery',
        backref=db.backref('authors', lazy=True))

    def __str__(self):
        return f"<Author {self.id}, {self.name}>"

    def get_authors(self):
        data = Author.query.all()
        dict_list=[]
        for a in data:
            d={
            'id': a.id,
            'author': a.name,
            'title': a.books
            }
            dict_list.append(d)
        return dict_list

    def get_author(self, name):
        data = Author.query.filter_by(name=name).first()
        data_dict = {
            'id': data.id,
            'author': data.name,
            'title': data.books
        }
        return data_dict

    def post_author(self, name, books):
        u = Author(name=name, books=books)
        db.session.add(u)
        db.session.commit()

    def post_author_update(self, name, books):
        data = self.get_author(name)
        u = Author(name=name, books=books)
        db.session.delete(data)
        db.session.add(u)
        db.session.commit()