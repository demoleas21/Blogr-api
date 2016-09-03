from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.pyfile('_config.py')
db = SQLAlchemy(app)
