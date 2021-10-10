#from flask_sqlalchemy import model
from app import db, models

class DbBook():
    def __init__(self, model): 
        self.model = model

    def get_books(self):#works
        data = self.model.query.all()
        data = self.model._dict(data)
        return data

    def get_book(self, id):#works
        data = self.model.query.filter_by(id=id).first()
        data = self.model._dict(data)
        return data 

    def post_book(self, author, title, status):#works
        book = self.model(author=author, title=title, status=status)
        db.session.add(book)
        db.session.commit()

    def put_book_update(self, id, author, title, status):#works
        data = self.model.query.filter_by(id=id).first()
        book = self.model(author=author, title=title, status=status)
        db.session.delete(data)
        db.session.add(book)
        db.session.commit()

book = DbBook(model=models.Book)