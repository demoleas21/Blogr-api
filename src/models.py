from datetime import datetime
from src import db


class Comment(db.Model):
    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    posted_date = db.Column(db.Date, default=datetime.utcnow())

    def __init__(self, comment, author, posted_date):
        self.comment = comment
        self.author = author
        self.posted_date = posted_date
