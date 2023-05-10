from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class LoginForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])

class CommentForm(FlaskForm):
    guestname = StringField("Имя", validators=[DataRequired()])
    text = TextAreaField("Текст комментария", validators=[DataRequired()])
