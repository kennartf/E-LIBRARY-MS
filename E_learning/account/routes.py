from flask import Blueprint
from E_learning import db, app
from .form import UpdateAccount
from E_learning .models import User
from flask_login import current_user, login_required
from E_learning .img_utils.utility import save_picture
from flask import flash, redirect, render_template, request, url_for, request



user_account = Blueprint('user_account', __name__)



@user_account.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccount()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data #this scrip is resp to change email and username
        current_user.email = form.email.data #<^>
        db.session.commit()
        flash('Your account has been updated!', category='success')
        return redirect(url_for('dashbrd.dashboard'))
    elif request.method == 'GET':
        form.username.data = current_user.username #this script helps by repopulating the email usrname into the form
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('edit-profile.html', image_file=image_file, form=form)





