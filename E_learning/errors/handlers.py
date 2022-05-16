from flask import Blueprint
from flask import render_template



my_error_page = Blueprint('my_error_page', __name__)



@my_error_page.app_errorhandler(404)
def page_not_found(error):
    return render_template('404_error_page.html'), 404


@my_error_page.app_errorhandler(500)
def page_not_found(error):
    return render_template('500_error_page.html'), 500