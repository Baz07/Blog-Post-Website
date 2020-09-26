## Include User and Blog Post Model
from companyblog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

## For Login Authorization
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin): ## UserMixin For Login
    __tablename__ = "users"

    ## User ID
    id = db.Column(db.Integer, primary_key = True)
    ## User Image
    profile_image = db.Column(db.String(64), nullable=False, default = 'default_profile.png')
    ## User Email
    email = db.Column(db.String(64), unique = True, index =True)
    ## User name
    username = db.Column(db.String(64), unique = True, index = True)
    ## User Password
    password_hash = db.Column(db.String(128))
    ## Blogpost to user
    posts = db.relationship('BlogPost', backref = "author", lazy=True)

    ## Create User Instance
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username {self.username}"

class BlogPost(db.Model):
    
    users = db.relationship(User)

    ## Id of blogs
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) ## users: Table name
    date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    title = db.Column(db.String(100), nullable = False)
    text = db.Column(db.Text, nullable= False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"Post ID: {self.id} --Date: {self.date} --- {self.title}"