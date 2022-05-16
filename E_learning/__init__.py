import os
import sqlite3
from flask import Flask
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_login import login_manager, LoginManager
from E_learning.hidden.config import  mail_username, mail_password




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SECRET_KEY'] = 'd6ac11bed59b75a6bmn4310nvbv4454ab'
app.config['UPLOAD_DIRECTORY'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16MB
app.config['ALLOWED_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.gif']



app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config["MAIL_USERNAME"] = mail_username
app.config["MAIL_PASSWORD"] = mail_password
# app.config["MAIL_USERNAME"] = os.environ.get('EMAIL_USER')
# app.config["MAIL_PASSWORD"] =  os.environ.get('EMAIL_PASS')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False



mail = Mail(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = 'authent.login'
login_manager.init_app(app)
login_manager.login_message_category = 'info'



from E_learning.views.routes import view
from E_learning.img_utils.utility import pic_utils
from E_learning.account.routes import user_account
from E_learning.authentication.routes import authent
from E_learning.errors.handlers import my_error_page
from E_learning.studentsadmin_.routes import dashbrd
from E_learning.master_admin.routes import master_adm



app.register_blueprint(view, url_prefix='/')
app.register_blueprint(authent, url_prefix='/')
app.register_blueprint(dashbrd, url_prefix='/')
app.register_blueprint(pic_utils, url_prefix='/')
app.register_blueprint(master_adm, url_prefix='/')
app.register_blueprint(user_account, url_prefix='/')
app.register_blueprint(my_error_page, url_prefix='/')

