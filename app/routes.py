from app import app, db_service
from db_service import book, author
from flask import jsonify, abort, make_response, request

@app.route("/api/v1/lib/", methods=["GET"]) #nie działa, błąd importu(?)
def lib_list_api_v1():
    return book.get_books()

@app.route("/api/v1/lib/", methods=["POST"])
def post_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    post = {
        'title': request.json['title'],
        'author': request.json.get('author', ""),#dlaczego tu jest inna struktura?
        'status': request.json['status']
    }
    posts.create(post)
    return jsonify({'post': post})

@app.route("/api/v1/lib/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = posts.get(post_id)
    if not post:
        abort(404)
    return jsonify({'post': post})

@app.route("/api/v1/lib/<int:post_id>", methods=["PUT"])
def post_update(post_id):
    post = posts.get(post_id)
    if not post:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'description' in data and not isinstance(data.get('description'), str),
        'done' in data and not isinstance(data.get('done'), bool)
    ]):
        abort(400)
    post = {
        'title': data.get('title', post['title']),
        'description': data.get('description', post['description']),
        'done': data.get('done', post['done'])
    }
    posts.update(post_id, post)
    return jsonify({'post': post})
###

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

if __name__ == "__main__":
    app.run(debug=True)