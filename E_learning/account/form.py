from flask_wtf import FlaskForm
from E_learning .models import User
from flask_login import current_user
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import Email, EqualTo, Length, ValidationError, DataRequired




class UpdateAccount(FlaskForm):
    username = StringField(validators=[DataRequired()], 
    render_kw={'autofocus': True, 'placeholder': 'Username'})
    email = StringField(validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email address'})
    picture = FileField(label='Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField(label='Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username already exist! Please try a different username')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email already exist Please choose different one')







