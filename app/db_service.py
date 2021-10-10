from operator import mod
from app import db, models

class DbBook():
    def __init__(self):
        pass

    def get_books(self):#works
        data = models.Book.query.all()
        data = models.Book._dict(data)
        return data

    def get_book(self, title):#works
        data = models.Book.query.filter_by(title=title).first()
        data = models.Book._dict(data)
        return data 

    def post_book(self, author, title, status):#works
        u = models.Book(author=author, title=title, status=status)
        db.session.add(u)
        db.session.commit()

    def put_book_update(self, author, title, status):#works
        data = models.Book.query.filter_by(title=title).first()
        u = models.Book(author=author, title=title, status=status)
        db.session.delete(data)
        db.session.add(u)
        db.session.commit()

book = DbBook()

class DbAuthor():
    def __init__(self):
        pass
    
    def get_authors(self):#works
        data = models.Author.query.all()
        data = models.Author._dict(data)
        return data

    def get_author(self, name):#works
        data = models.Author.query.filter_by(name=name).first()
        data = models.Author._dict(data)
        return data

    def post_author(self, name, books):#works
        u = models.Author(name=name, books=books)
        db.session.add(u)
        db.session.commit()

    def put_author_update(self, name, books):#works
        data = models.Author.query.filter_by(name=name).first()
        u = models.Author(name=name, books=books)
        db.session.delete(data)
        db.session.add(u)
        db.session.commit()

author = DbAuthor()