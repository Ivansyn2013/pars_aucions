from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators, SelectMultipleField, HiddenField


class RegisterUserForm(FlaskForm):
    first_name = StringField(
        'Имя',
        [validators.DataRequired()],
    )
    last_name = StringField(
        'Фамилия',
        [validators.DataRequired()],
    )
    username = StringField(
        'Псевдоним',
        [validators.DataRequired()],
    )

    email = StringField(
        'email',
        [validators.DataRequired(),
         validators.email()],
    )

    submit = SubmitField("Создать")
