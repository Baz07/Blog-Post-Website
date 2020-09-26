from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed ## for Profile Picture Updation


from flask_login import current_user
from companyblog.models import User

class LoginForm(FlaskForm):
    email = StringField("Email ID", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("LogIn!")

class RegistrationForm(FlaskForm):
    email = StringField("Email ID", validators=[DataRequired(), Email()])
    username = StringField("UserName", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("pass_confirm", message="Passwords must match!")])
    pass_confirm = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Register!")
    ## check for email
    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("Already Registered Email!")
    
    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("Already Registered Username!")

class UpdateUserForm(FlaskForm):
    email = StringField("Email ID", validators=[DataRequired(), Email()])
    username = StringField("UserName", validators=[DataRequired()])
    picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField("Update")

    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("Already Registered Email!")
    
    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("Already Registered Username!")
