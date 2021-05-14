from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# so flask knows where to look for templates and static files
app = Flask(__name__)

# make an environment variable later
app.config['SECRET_KEY'] = 'fdc03f61e31fac890e1e89617fabac1e'
# "///" means relative path from current file (i.o.w, same directory)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)  # database instance
# (in terminal)
# import secrets
# secrets.token_hex(16)  16 is the number of bytes

from flaskblog import routes