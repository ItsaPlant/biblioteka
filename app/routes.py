from app import app, models
from app.db_service.book import book as db_book
from app.db_service.author import author as db_author
from flask import jsonify, abort, make_response, request

###book - libary -> /api/v1/lib/
@app.route("/api/v1/lib/", methods=["GET"])#works
def lib_list_api_v1():
    return jsonify(db_book.get_books())

@app.route("/api/v1/lib/", methods=["POST"])
def post_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'title': request.json['title'],
        'author': request.json['author'], #dlaczego tu oryginalnie jest inna struktura?
        'status': request.json['status']
    }
    db_book.post_book(author=book['title'], title=book['title'], status=book['status'])
    return jsonify({'book': book})

@app.route("/api/v1/lib/<int:id>", methods=["GET"])#works
def get_book(id):
    book = db_book.get_book(id)
    if not book:
        abort(404)
    return jsonify({'book': book})

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
        'title': data.get('title', book['title']),
        'author': data.get('author', book['author']),
        'status': data.get('status', book['status'])
    }
    db_book.put_book_update(id, author=book['author'], title=book['title'], status=book['status'])
    return jsonify({'post': book})

###author - bibliography -> /api/v1/bibl/
@app.route("/api/v1/bibl/", methods=["GET"])#works
def bibl_list_api_v1():
    return jsonify(db_author.get_authors())

@app.route("/api/v1/bibl/", methods=["POST"])#works
def post_author():
    if not request.json or not 'title' in request.json:
        abort(400)
    auth = {
        'title': request.json['title'],
        'author': request.json['author'] #dlaczego tu oryginalnie jest inna struktura?
    }
    db_author.post_author(name=auth['author'], books=auth['title'])
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
        'title' in data and not isinstance(data.get('title'), str),
        'author' in data and not isinstance(data.get('author'), str)
    ]):
        abort(400)
    auth = {
        'title': data.get('title', auth['title']),
        'author': data.get('author', auth['author'])
    }
    db_author.put_author_update(id, name=auth['author'], books=auth['title'])
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