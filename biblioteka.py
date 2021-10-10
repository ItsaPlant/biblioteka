from app import app, db
from app.models import Book, Author
from app.db_service.book import DbBook
from app.db_service.author import DbAuthor

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Book": Book,
        "Author": Author,
        "DbBook": DbBook,
        "DbAuthor": DbAuthor
    }