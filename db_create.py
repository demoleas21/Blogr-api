from src.api import db
from src.models import Comment
from datetime import datetime

db.create_all()
db.session.add(Comment('Test Comment', 'admin', datetime.utcnow()))
db.session.commit()
