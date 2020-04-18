from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField,PasswordField,SelectField
from wtforms.validators import DataRequired
from wtforms.validators import Email
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired

class UploadForm(FlaskForm):
 description = TextAreaField('Description', validators=[DataRequired()])
 photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])
    ])