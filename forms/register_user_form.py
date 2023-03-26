from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators, SelectMultipleField, HiddenField


class RegisterUserForm(FlaskForm):
    name = StringField(
        'Имя',
        [validators.DataRequired()],
    )
    status = TextAreaField(
        "Статус",
        [validators.DataRequired()],
    )
    auctions = SelectMultipleField('Аукцион', coerce=str)
    users = SelectMultipleField('Пользователи', coerce=str)

    submit = SubmitField("Создать")
