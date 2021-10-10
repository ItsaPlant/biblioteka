from app import app, db
from app.models import Book, Author
from app.db_service import DbBook, DbAuthor

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Book": Book,
        "Author": Author,
        "DbBook": DbBook,
        "DbAuthor": DbAuthor
    }