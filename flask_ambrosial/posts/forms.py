#!/usr/bin/env python3

"""
Forms for creating posts, comments, and replies in the Flask application.
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    """
    Form for creating a new post.
    """
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    image_filename = FileField(
        'Image', validators=[
            DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])
        ]
    )
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    """
    Form for creating a new comment.
    """
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Comment')

class ReplyForm(FlaskForm):
    """
    Form for creating a new reply.
    """
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Reply')
