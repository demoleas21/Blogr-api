from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('_config.py')
db = SQLAlchemy(app)

from src.models import Comment


@app.route('/comments', methods=['GET'])
def get_comments():
    results = db.session.query(Comment).limit(10).offset(0).all()
    json_results = []
    for result in results:
        data = {
            'comment_id': result.comment_id,
            'comment': result.comment,
            'author': result.author,
            'posted_date': result.posted_date
        }
        json_results.append(data)
    return jsonify(comments=json_results)


@app.route('/comments/<int:comment_id>', methods=['GET'])
def get_individual_comment(comment_id):
    results = db.session.query(Comment).filter_by(comment_id=comment_id)
    json_results = []
    for result in results:
        data = {
            'comment_id': result.comment_id,
            'comment': result.comment,
            'author': result.author,
            'posted_date': result.posted_date
        }
        json_results.append(data)
    return jsonify(comments=json_results)


@app.route('/comments', methods=['POST'])
def post_comments():
    new_comments = Comment(
        request.form['comment'],
        request.form['author'],
        datetime.utcnow()
    )
    db.session.add(new_comments)
    db.session.commit()
    return jsonify(new_comments.toDictionary())


@app.route('/comments/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    comments = db.session.query(Comment).filter_by(comment_id=comment_id)
    updated_comment = request.form['comment']
    for comment in comments:
        comment.comment = updated_comment
    # updated_author = request.form['author']
    # comment.author = updated_author
    db.session.commit()
    return jsonify(comment.toDictionary())
