from app import app, models
from app.db_service.book import db_book
from app.db_service.author import db_author
from flask import jsonify, abort, make_response, request
import json

###book - libary -> /api/v1/lib/
@app.route("/api/v1/lib/", methods=["GET"])#works
def lib_list_api_v1():
    return json.dumps(db_book.get_books())

@app.route("/api/v1/lib/", methods=["POST"])
def post_book():
    if not request.json or not all('title' in row for row in request.json):
        abort(400)
    book = {
        'title': request.json[0]['title'],
        'author': request.json[0]['author'], #dlaczego tu oryginalnie jest inna struktura?
        'status': request.json[0]['status']
    }
    db_book.post_book(author=book['title'], title=book['title'], status=book['status'])
    return json.dumps({'book': book})

@app.route("/api/v1/lib/<int:id>", methods=["GET"])#works
def get_book(id):
    book = db_book.get_book(id)
    if not book:
        abort(404)
    return json.dumps({'book': book})

@app.route("/api/v1/lib/<int:id>", methods=["PUT"])#works
def put_book_update(id):
    book = db_book.get_book(id)
    if not book:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'author' in data and not isinstance(data.get('author'), str),
        'status' in data and not isinstance(data.get('status'), str)
    ]):
        abort(400)
    book = {
        'title': data[0].get('title', book['title']),
        'author': data[0].get('author', book['author']),
        'status': data[0].get('status', book['status'])
    }
    db_book.put_book_update(id, author=book['author'], title=book['title'], status=book['status'])
    return jsonify({'post': book})

###author - bibliography -> /api/v1/bibl/
@app.route("/api/v1/bibl/", methods=["GET"])#works
def bibl_list_api_v1():
    return json.dumps(db_author.get_authors())

@app.route("/api/v1/bibl/", methods=["POST"])#works
def post_author():
    if not request.json or not all('name' in row for row in request.json):
        abort(400)
    auth = {
        'name': request.json[0]['name'],
        'books': request.json[0]['books'] #dlaczego tu oryginalnie jest inna struktura?
    }
    db_author.post_author(name=auth['name'], books=auth['books'])
    return jsonify({'author': auth})

@app.route("/api/v1/bibl/<int:id>", methods=["GET"])#works
def get_author(id):
    auth = db_author.get_author(id)
    if not auth:
        abort(404)
    return jsonify({'author': auth})

@app.route("/api/v1/bibl/<int:id>", methods=["PUT"])#works
def put_author_update(id):
    auth = db_author.get_author(id)
    if not auth:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'name' in data and not isinstance(data.get('name'), str),
        'books' in data and not isinstance(data.get('books'), str)
    ]):
        abort(400)
    auth = {
        'name': data[0].get('name', auth['name']),
        'books': data[0].get('books', auth['books'])
    }
    db_author.put_author_update(id, name=auth['name'], books=auth['books'])
    return jsonify({'author': auth})

###errorhadler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

if __name__ == "__main__":
    app.run(debug=True)