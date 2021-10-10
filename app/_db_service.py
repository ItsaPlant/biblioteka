from flask_sqlalchemy import model
from app import db, models

class DbBook():
    def __init__(self, model): 
        pass

    def get_books(self):#works
        data = model.query.all()
        data = model._dict(data)
        return data

    def get_book(self, id):#works
        data = model.query.filter_by(id=id).first()
        data = model._dict(data)
        return data 

    def post_book(self, author, title, status):#works
        book = model(author=author, title=title, status=status)
        db.session.add(book)
        db.session.commit()

    def put_book_update(self, id, author, title, status):#works
        data = model.query.filter_by(id=id).first()
        book = model(author=author, title=title, status=status)
        db.session.delete(data)
        db.session.add(book)
        db.session.commit()

book = DbBook(model=models.Book)

class DbAuthor():
    def __init__(self, model):
        pass
    
    def get_authors(self):#works
        data = model.query.all()
        data = model._dict(data)
        return data

    def get_author(self, id):#works
        data = model.query.filter_by(id=id).first()
        data = model._dict(data)
        return data

    def post_author(self, name, books):#works
        auth = model(name=name, books=books)
        db.session.add(auth)
        db.session.commit()

    def put_author_update(self, id, name, books):#works
        data = model.query.filter_by(id=id).first()
        auth = model(name=name, books=books)
        db.session.delete(data)
        db.session.add(auth)
        db.session.commit()

author = DbAuthor(model=models.Author)