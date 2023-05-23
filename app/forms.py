from flask_wtf import FlaskForm #datatype = CLASS
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    pass