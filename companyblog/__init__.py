## companyblog/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecret"

##################
## Database ######
##################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


##################
##Login COnfig####
##################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login" ## Inside Users View


## register Core Blueprint
from companyblog.core.views import core
from companyblog.error_pages.handlers import error_pages
from companyblog.users.views import users
from companyblog.blogpost.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(blog_posts)