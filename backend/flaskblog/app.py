import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_mail import Mail
from filters import datetimeformat, file_type

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS')
mail = Mail(app)

ENV = 'dev'
if ENV == 'dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI']

elif ENV == 'stage':
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI']

elif ENV == 'prod':
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI']

app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['file_type'] = file_type

from users.routes import users
from posts.routes import posts
from main.routes import main
from files.routes import files
from errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(files)
app.register_blueprint(errors)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')