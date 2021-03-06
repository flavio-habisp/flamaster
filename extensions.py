from __future__ import absolute_import
from flask.ext.babel import Babel, gettext, ngettext
from flask.ext.cache import Cache
from flask.ext.mail import Mail
from flask.ext.mongoengine import MongoEngine
from flask.ext.redis import Redis
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security
from flask.ext.social import Social
from flask.ext.elasticsearch import ElasticSearch
from flask.ext.s3 import FlaskS3
from raven.contrib.flask import Sentry

def register_jinja_helpers(app):
    app.jinja_env.globals.update({
        '_': gettext,
        '__': ngettext
    })


babel = Babel()
cache = Cache()
db = SQLAlchemy()
mail = Mail()
mongo = MongoEngine()
es = ElasticSearch()
redis = Redis()
security = Security()
social = Social()
s3 = FlaskS3()
sentry = Sentry()
