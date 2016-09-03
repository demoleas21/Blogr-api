import os

basedir = os.path.absolute(os.path.dirname(__file__))

DATABASE = 'blogr.db'
WTF_CSRF_ENABLED = True
SECRET_KEY = '\x93v\xdc\xb9\x8f\xd6a\x12/\xff\x12LM\xf8\x23\xf5\xe2\xbe\x84\xc0G\xe5`\xa6'

DATABASE_PATH = os.path.join(basedir, DATABASE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH