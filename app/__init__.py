#from flask import Flask
#
#app = Flask(__name__)
#app.config.from_object('config')
#
#from app import views

#
#import sqlalchemy
#
#from flask import Flask
#
#
#
#
#
#
#

import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir
from flask import Flask
import config
import telnet_connector as tconn


app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

oid = OpenID(app, os.path.join(basedir, 'tmp'))


k = {'password': config.PASS,
     'host': config.HOST,
     'port': config.PORT}
connector = tconn.Settinger(**k)

import views, models
