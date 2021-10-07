from app import db
from models import Book, Author

class Db_book(Book):
    def __init__(self):
        super().__init__()

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

book = Db_book()

class Db_author(Author):
    def __init__(self):
        super().__init__()
    
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

author = Db_author()