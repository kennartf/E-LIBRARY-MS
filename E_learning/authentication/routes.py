from flask import Blueprint
from flask_mail import Message
from E_learning import db, bcrypt, mail
from flask import get_flashed_messages
from E_learning .models import User, Mybook
from flask import flash, redirect, render_template, request, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from .form import RegisterForm, LoginForm, RequestResetForm, ResetPasswordForm, Studentbrq


authent = Blueprint('authent', __name__)



@authent.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data)
        user = User(index=form.index.data,  username=form.username.data, email=form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully {user.email}', category='success')
        return redirect(url_for('authent.login'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Registration unsuccessful {err_msg}', category='error')
    return render_template('signup_.html', form=form)
 


@authent.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(index=form.index.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Successfully logged in as {user.index}', category='success')
            return redirect(url_for('dashbrd.dashboard'))
        else:
            flash('Login Uncessful. Please check email and password', category='error')
    return render_template('login.html', form=form)




@authent.route('/bkrequest', methods=['GET', 'POST'])
def  bkrequest():
    form = Studentbrq()
    if form.validate_on_submit():
        usrb = Mybook(the_title=form.the_title.data, thebook_auth=form.thebook_auth.data, 
                                        dpment=form.dpment.data, author=current_user)
        db.session.add(usrb)
        db.session.commit()
        flash(f'Your request has been submited! you will receive the feedback', category='success')
        return redirect(url_for('dashbrd.dashboard'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Oops there's a problem! try again {err_msg}", category='error')
    return render_template('bookrequest.html', form=form)
    



def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='geniusitg@gmail.com', recipients=[user.email])
    msg.body =  f''' To reset your password, visit the following link: {url_for('authent.reset_token', 
    token=token, _external=True)}
    If you did not make this request then simply ignore this email and no changes will be made. '''
    mail.send(msg) 


@authent.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password', category='info')
        return redirect(url_for('authent.login'))
    return render_template('reset_request.html', form=form)


@authent.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', category='warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data)
        user.password = hashed_pwd
        db.session.commit()
        flash(f'Your password has been update! You are now able to log in', category='success')
        return redirect(url_for('authent.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)



@authent.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out successfuly', category='success')
    return render_template('home.html')
