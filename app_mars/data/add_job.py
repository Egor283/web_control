from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    job = StringField('Название работы', validators=[DataRequired()])
    team_leader = IntegerField('ID тимлида', validators=[DataRequired()])
    work_size = StringField('Длительность работы', validators=[DataRequired()])
    collaborators = StringField('Коллаборация', validators=[DataRequired()])
    is_finished = BooleanField('Закончена ли работа?')
    submit = SubmitField('Добавить работу')