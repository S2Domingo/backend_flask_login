from socketserver import DatagramRequestHandler
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

# User Login
class UserLoginForm(FlaskForm):
    user_id = StringField('사용자 아이디', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('비밀번호', validators=[DataRequired()])
