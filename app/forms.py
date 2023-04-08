# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField 
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Desctiption', validators=[InputRequired()])
    poster = FileField('Poster', validators=[FileRequired(), FileAllowed(['jpg','JPG','png','PNG'],'JPG OR PNG FILES ONLY!')])