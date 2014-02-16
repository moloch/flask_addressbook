"""
    Application module init
    ~~~~~~~~~~~~~~

    Package-wide app and db objects are provided to all modules
    

    :copyright: (c) 2014 by Dario Coco
    :license: GPLv3, see LICENSE for more details.
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=False,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
))

db = SQLAlchemy(app)

import views