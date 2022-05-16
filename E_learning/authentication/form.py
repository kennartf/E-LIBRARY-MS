from flask_wtf import FlaskForm
from E_learning .models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import Email, EqualTo, Length, ValidationError, DataRequired
from wtforms import StringField, SelectField, SubmitField, PasswordField, BooleanField, TextAreaField




class RegisterForm(FlaskForm):
    index = StringField(validators=[DataRequired(), Length(min=1, max=10)],  
                                            render_kw={'autofocus': True, 'placeholder': 'Student Id'})
    username = StringField(validators=[DataRequired(), Length(min=2, max=30)],  
                                            render_kw={'autofocus': True, 'placeholder': 'Username (2-30 characters)'})
    email = StringField(validators=[DataRequired(), Email()], 
                                            render_kw={'placeholder': 'Email address'})
    password = PasswordField(validators=[DataRequired(), Length(min=2, max=30)], 
                                            render_kw={'placeholder': 'Password (2-30 characters)'})
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password')], 
                                            render_kw={'placeholder': 'Confirm_Password'})
    submit = SubmitField(label='Sign Up')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username already exist! Please try a different username')


    def validate_index(self, index):
        user = User.query.filter_by(index=index.data).first()
        if user:
            raise ValidationError('That index number already exist! Please try a different index num.')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email already exist Please choose different one')



class LoginForm(FlaskForm):
    index = StringField(validators=[DataRequired()], 
    render_kw={'autofocus': True, 'placeholder': 'Student Id'})
    password = PasswordField(validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    remember = BooleanField(label='Remember')
    submit = SubmitField(label='Log In')



class Studentbrq(FlaskForm):
    the_title = StringField(validators=[DataRequired()], render_kw ={'autofocus': True, 'placeholder': 'Book title'})
    thebook_auth = StringField(validators=[DataRequired()], render_kw={'placeholder': 'Book author'})
    dpment = StringField(validators=[DataRequired()], render_kw={'placeholder': 'Category'})
    submit = SubmitField(label='Send Request')



class RequestResetForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()], 
    render_kw={'autofocus': True, 'placeholder': 'Please enter your valid email address'})
    submit = SubmitField(label='Request Password Reset')

    def validate_email(self, email):
            user = User.query.filter_by(email=email.data).first()
            if user is None:
                raise ValidationError('There is no account with that email')



class ResetPasswordForm(FlaskForm):
    password = PasswordField(validators=[DataRequired(), Length(min=2, max=30)], 
    render_kw={'autofocus': True, 'placeholder':'Password (must be at least 10-20 characters)'})
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password')], render_kw={'placeholder':'Confirm_Password'})
    submit = SubmitField(label='Reset Password')