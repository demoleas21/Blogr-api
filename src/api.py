from flask import Flask, flash, redirect, jsonify, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('_config.py')
db = SQLAlchemy(app)

from src.models import Comment


@app.route('/', methods=['GET'])
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
    return jsonify(items=json_results)


@app.route('/post', methods=['POST'])
def post_comments():
    pass
