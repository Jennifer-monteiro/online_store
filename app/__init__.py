from flask import Flask
from config import Config
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager
from .models import db, User



app = Flask(__name__)
app.config.from_object(Config)
app.static_folder = 'static'


# Initialize SQLAlchemy, Bcrypt, Migrate, and LoginManager
db.init_app(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Set the login view
@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()



# Import all routes / models

from app.admin import routes
from app.products import routes
from app.products.models import Brand, Category, Product

# ...



