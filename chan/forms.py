from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError


class ThreadForm(FlaskForm):
    name = StringField(label="Username")
    text = TextAreaField(label="Comment", validators=[DataRequired()])
    submit = SubmitField(label="Post")


class RepliesForm(FlaskForm):
    name = StringField(label="Username")
    text = TextAreaField(label="Comment", validators=[DataRequired()])
    submit = SubmitField(label="Post")
