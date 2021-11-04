__version__ = '0.1.0'

from flask import Flask
from flask_script import Manager

# from flaskext.mysql import MySQL
import os

app = Flask(__name__)
app.config.from_pyfile("config.py")


manager = Manager(app)
# mysql = MySQL(app)


from edu-kalculadora.controllers import urls
from edu-kalculadora.models import tables
