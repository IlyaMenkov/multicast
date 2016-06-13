from app import db
import datetime
ROLE_USER = 0
ROLE_ADMIN = 1

SIMPLE = 0
ON_DEMAND = 1
Scheduled = 2

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    posts = db.relationship('Post', backref='author', lazy='dynamic')



    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id) # python 2
        except NameError:
            return str(self.id) # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    path = db.Column(db.String(140))
    ip_addr = db.Column(db.String(140))
    type = db.Column(db.SmallInteger, default=SIMPLE)
    dt = db.Column(db.String(140), default=None)

    def __repr__(self):
        return '<Post %r>' % (self.name)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    path = db.Column(db.String(140))
    ip_address = db.Column(db.String(140))

    def __repr__(self):
        return '<Post %r>' % (self.body)