from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, EmailField, StringField
from wtforms.validators import DataRequired

class Registr_form(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    password_again = PasswordField("Пароль", validators=[DataRequired()])
    surname = SubmitField("Фамилия", validators=[DataRequired()])
    name = SubmitField("Имя", validators=[DataRequired()])
    age = SubmitField("Возраст", validators=[DataRequired()])
    position = SubmitField("Позиция", validators=[DataRequired()])
    speciality = SubmitField("Специальность", validators=[DataRequired()])
    address = SubmitField("Адресс", validators=[DataRequired()])
    submit = SubmitField("Войти")