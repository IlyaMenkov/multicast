import os
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI for flask-SQLAlchemy. path to database file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# SQLALCHEMY_MIGRATE_REPO - dirrectory where we sill contain SQLAlchemy-migrate files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#  secret key needs only when CSRF_ENABLED = True
CSRF_ENABLED = True
SECRET_KEY = 'lollypop'

OPENID_PROVIDERS = [
    {'name': 'openid', 'url': 'https://openid.stackexchange.com/'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

HOST = 'localhost'
PORT = '4212'
PASS = '123'