from flask import Flask
from config import Config, DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app.models import Products

admin = Admin(app)
admin.add_view(ModelView(Products, db.session))

from app import routes, models