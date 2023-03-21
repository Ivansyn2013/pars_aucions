from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators, SelectMultipleField

class CreateProjectForm(FlaskForm):
    name = StringField(
        'Имя',
        [validators.DataRequired()],
    )
    status = TextAreaField(
        "Статус",
        [validators.DataRequired()],
    )
    auctions =  SelectMultipleField('Аукцион', coerce=str)
    users = SelectMultipleField('Пользователи', coerce=str)

    submit = SubmitField("Создать")