from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators, SelectMultipleField

class CreateProjectForm(FlaskForm):
    name = StringField(
        'Title',
        [validators.DataRequired()],
    )
    status = TextAreaField(
        "Body",
        [validators.DataRequired()],
    )
    auctions = 'здесь должно быть поле с выбором или номер тогда надо функцию вызывать'
    users = SelectMultipleField(

    )

    submit = SubmitField("Publish")