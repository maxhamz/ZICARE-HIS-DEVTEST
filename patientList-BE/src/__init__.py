from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from src.config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager
# from flask_serialize import FlaskSerializeMixin
# instantiate the extensions
cors = CORS()

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app():
    app = Flask(__name__)
    cors.init_app(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    jwt = JWTManager(app)

    migrate = Migrate(app, db)
    
    from src.users.routes import users
    from src.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(errors)

    return app