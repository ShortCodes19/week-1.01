from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'c43b83c0293d2411af1a4f29f8f12cc1'
    app. config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/// blog.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = True

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    