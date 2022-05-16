import os
from flask import Blueprint
from E_learning import db, app
from flask_login import login_required, current_user
from E_learning .img_utils.utility import save_picture
from .form import Sbookupload, Allbooks, Approvebook
from E_learning .models import User, Bokitems, Mybook, Bokitems
from flask import render_template, flash, request, redirect, url_for, send_from_directory



dashbrd = Blueprint('dashbrd', __name__)



@dashbrd.route('/htuADmin2022', methods=['POST', 'GET'])
@login_required
def htuADmin2022():
    if request.method == 'GET':
        query = request.args.get('query')     
        post = Bokitems.query.filter(Bokitems.stb_title.like('%' + str(query)+ '%')).all()
        flash(f'You have searched for {query}', category='success' )
    else:
        flash("Your search doesn't much the request", category='danger')
    return render_template('adminlog.html', posts=post , query=query)




@dashbrd.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    student_books = Bokitems.query.all()
    if request.method == 'GET':
        query = request.args.get('query')
        posts = Bokitems.query.filter(Bokitems.stb_title.like('%' + str(query) + '%')).all()
    return render_template('dashboard.html', student_books=student_books, posts=posts, query=query)



@dashbrd.route('/addbook', methods=['GET', 'POST'])
@login_required
def addbook():
    form = Sbookupload()
    if form.validate_on_submit():
        usrb = Bokitems(stb_title=form.stb_title.data,  th_auth=form.th_auth.data,  
                                            my_category=form.my_category.data, 
                                            nm_issuerer=form.nm_issuerer.data, 
                                            author=current_user, bok_profile=save_picture(form.bok_profile.data))
        db.session.add(usrb)
        db.session.commit()
        flash('Your data has been added to the system', category='success')
        return redirect(url_for('dashbrd.htuADmin2022'))
    if form.errors !={}:
        for err_msg in form.errors.values():
            flash(f'Your request was not sent please try again {err_msg}', category='error')
    return render_template('addbook.html', form=form)



@dashbrd.route('/allbooks')
@login_required
def allbooks():
    form = Allbooks()
    student_books = Bokitems.query.order_by(Bokitems.id.desc()).all()
    return render_template('allbooks.html', form=form, student_books=student_books)



@dashbrd.route('/approve')
@login_required
def approve():
    form = Approvebook()
    users = User.query.all()
    return render_template('approve.html', form=form, users=users)



@dashbrd.route('/request_all')
@login_required
def request_all():
    students = Mybook.query.order_by(Mybook.date_request.desc()).all()
    dir(students)
    return render_template('request_all_book.html', students=students)