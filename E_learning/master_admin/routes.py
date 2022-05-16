from flask import Flask
from flask import Blueprint
from E_learning import db, bcrypt
from .form import AdminLogin, AdminReg
from E_learning.models import AdminSession
from flask_login import login_user, login_required, current_user
from flask import render_template, redirect, flash, request, url_for



master_adm = Blueprint('master_adm', __name__)





@master_adm.route('/htuADmin2022/<int:post_id>', methods=['GET', 'POST'])
def adsignup(post_id):
    form = AdminReg()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data)
        user = AdminSession(staffid=form.staffid.data,  password=hashed_pwd, is_admin=True)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully {user.staffid}', category='success')
        return redirect(url_for('master_adm.logme'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Registration unsuccessful {err_msg}', category='error')
    return render_template('supperreg.html', form=form)




# 12345
@master_adm.route('/logme', methods=['GET', 'POST'])
def logme():
    form = AdminLogin()
    if form.validate_on_submit():
        user = Master.query.filter_by(staffid=form.staffid.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'Successfully logged in as {user.staffid}', category='success')
            return redirect(url_for('dashbrd.admin'))
        else:
            flash('Login Uncessful. Please check email and password', category='error')
    return render_template('supperlogin.html', form=form)
