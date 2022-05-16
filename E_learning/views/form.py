from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import Email, EqualTo, Length, ValidationError, DataRequired



class ContactForm(FlaskForm):
    name = StringField(validators=[DataRequired()], render_kw={'placeholder': 'Your name'})
    student_id = StringField(validators=[DataRequired(), Email()], render_kw={'placeholder': 'student ID'})
    subject = StringField(validators=[DataRequired()], render_kw={'placeholder': 'subject'})
    phone_number = StringField(validators=[DataRequired()], render_kw={'placeholder': 'phone numbers'})
    text_area = TextAreaField(validators=[DataRequired()], render_kw={'placeholder': 'Comments, suggestion hear'})
    submit = SubmitField(label='Submit')






