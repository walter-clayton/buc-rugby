# import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager

# MIGRATION_DIR = os.path.join('models', 'migrations')

# configuration

# instantiate the app
# app.config.from_object(__name__)
# db.init_app(app)
# migrate = Migrate(app, db, directory=MIGRATION_DIR)
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from backend import routes