from E_learning import db
from flask import Blueprint
from E_learning import bcrypt
from .form import ContactForm
from E_learning .models import Bokitems
from flask_login import login_user, current_user
from E_learning .models import User, Suggestion_Contact
from flask import render_template, request, url_for, flash, redirect



view = Blueprint('view', __name__)


@view.route('/')
@view.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')



@view.route('/books')
def books():
    return render_template('books.html')



@view.route('/mechanical')
def mechanical():
    redirect('view.dashboard')
    return render_template('mech.html')



@view.route('/fashion')
def fashion():
    redirect('view.dashboard')
    student_books = Bokitems.query.all()
    return render_template('fahiondepart.html', student_books=student_books)


 
@view.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        cont = Suggestion_Contact(name=form.name.data, student_id=form.student_id.data, 
                                                                subject=form.subject.data, 
                                                                phone_number=form.phone_number.data, 
                                                                text_area=form.text_area.data, author=current_user)
        db.session.add(cont)
        db.session.commit()
        flash('Thanks for your suggestion our team will work on it', category='success')
        return redirect(url_for('view.home'))
    return render_template('contact.html', form=form)



@view.route('/about')
def about():
    return render_template('about.html')
