from app import db, models


class DbAuthor():
    def __init__(self, model):
        self.model = model
    
    def get_authors(self):#works
        data = self.model.query.all()
        data = self.model._dict(data)
        return data

    def get_author(self, id):#works
        data = self.model.query.filter_by(id=id).first()
        data = self.model._dict(data)
        return data

    def post_author(self, name, books):#works
        auth = self.model(name=name, books=books)
        db.session.add(auth)
        db.session.commit()

    def put_author_update(self, id, name, books):#works
        data = self.model.query.filter_by(id=id).first()
        auth = self.model(name=name, books=books)
        db.session.delete(data)
        db.session.add(auth)
        db.session.commit()

db_author = DbAuthor(model=models.Author)