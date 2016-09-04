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


@app.route('/post', methods=['POST'])
def post_comments():
    new_comments = Comment(
        request.json['comment'],
        request.json['author'],
        datetime.utcnow()
    )
    db.session.add(new_comments)
    db.session.commit()
    return 'POST Successful'
