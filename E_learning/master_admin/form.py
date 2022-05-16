from flask_wtf import FlaskForm
from E_learning .models import AdminSession
from wtforms import StringField, SubmitField, FileField, PasswordField, BooleanField
from wtforms.validators import Email, EqualTo, DataRequired, Length, ValidationError



class AdminReg(FlaskForm):
    staffid = StringField(validators=[DataRequired(), Length(min=1, max=10)],  
    render_kw={'autofocus': True, 'placeholder': 'Staff ID'})
    password = PasswordField(validators=[DataRequired(), Length(min=2, max=15)], render_kw={'placeholder': 'Password'})
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password')], render_kw={'placeholder': 'Confirm_Password'})
    submit = SubmitField(label='Sign Up')



    # def validate_username(self, adminid):
    #     user = User.query.filter_by(adminid=adminid.data).first()
    #     if user:
    #         raise ValidationError('That ID already exist! Please try a different username')



class AdminLogin(FlaskForm):
    staffid = StringField(validators=[DataRequired(), Length(min=8, max=15)],
     render_kw={'autofocus': True, 'placeholder': 'Staff Id'})
    password = PasswordField(validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    submit = SubmitField(label='Sign In')


