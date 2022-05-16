from flask_wtf import FlaskForm
from E_learning .models import User
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length
from wtforms import SubmitField, StringField, TextAreaField, SelectField



class Sbookupload(FlaskForm):
    stb_title = StringField(validators=[DataRequired()], render_kw={'autofocus': True, 'placeholder': "Book title"})
    th_auth = StringField(validators=[DataRequired()], render_kw={'placeholder': 'Book author'})
    my_category = StringField(validators=[DataRequired()], render_kw={'placeholder': 'Book category'})
    nm_issuerer = StringField(validators=[DataRequired()], render_kw={'placeholder':'Issuer'})
    bok_profile = FileField(label='File Upload', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField(label='Submit Form')


class Allbooks(FlaskForm):
    departments = SelectField('', validators=[DataRequired()], choices=[('Select', 'select'),
     ('Computer Science', 'Computer Science'), ('Fahion', 'Fahion'), ('Industrial', 'Industrial'), ('Mechanical', 'Mechanical'), ('Agro', 'Agro')])


class Approvebook(FlaskForm):
    departments = SelectField('', validators=[DataRequired()], choices=[('Select', 'select'),
     ('Computer Science', 'Computer Science'), ('Fahion', 'Fahion'), ('Industrial', 'Industrial'), ('Mechanical', 'Mechanical'), ('Agro', 'Agro')])
