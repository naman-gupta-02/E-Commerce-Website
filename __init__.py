from flask_login import LoginManager
from run import app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
db.init_app(app)

bcrypt = Bcrypt()
bcrypt.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
login_manager.init_app(app)