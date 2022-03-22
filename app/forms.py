from distutils.command.upload import upload
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class AddProperty(FlaskForm):
    pic = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Must be an Image')])
    title = StringField('Title', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    type = SelectField('Property Type', choices = [('House','House'), ('Apartment','Apartment')],validators=[DataRequired()])
    bathroom_no = StringField('Number of Bathrooms', validators=[DataRequired()])
    bedroom_no = StringField('Number of Bedrooms', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    