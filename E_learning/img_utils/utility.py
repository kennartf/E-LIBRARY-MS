import os
import secrets
from PIL import Image 
from flask import Blueprint, flash
from E_learning import app
from flask_login import current_user



pic_utils = Blueprint('pic_utils', __name__)


def save_picture(form_picture):# from_picture is an agument that save our picture
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)# app.root_path gives the location of the piture path
    if os.path.exists(app.root_path +'/static/profile_pics/' + current_user.image_file):
        os.remove(app.root_path + '/static/profile_pics/' + current_user.image_file)

    output_size = (600, 600)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn
