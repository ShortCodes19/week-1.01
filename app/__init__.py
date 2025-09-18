from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy() # to be imported
login_manager = LoginManager() # to be imported

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app. config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = True

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Import Blueprints
    from app.auth.routes import auth
    from app.blog.routes import blog
    # from app.profile.routes import profile

    # Register the Blueprints
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(blog, url_prefix='/blog')
    # app.register_blueprint(profile, url_prefix='/profile')

    with app.app_context():
        db.create_all()

    # return app(must)
    return app