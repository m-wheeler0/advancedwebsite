from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])

    def validate_username(self, field):
        username = field.data
        user = User.query.filter_by(username=username).first()
        if user:
            raise ValidationError("This username is already taken, please choose a different username");
