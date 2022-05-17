from datetime import datetime
from datetime import datetime
from E_learning import db, app
from sqlalchemy.sql import func
from flask_admin import Admin
from flask_login import UserMixin
from E_learning import login_manager
from flask_admin.contrib.sqla import ModelView 
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, ForeignKey
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer



@login_manager.user_loader
def load_user(userr_id):
    return User.query.get(int(userr_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    index = db.Column(db.String(length=100), nullable=False, unique=True)
    username = db.Column(db.String(length=100), nullable=False, unique=True)
    email = db.Column(db.String(length=100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    image_file =db.Column(db.String(100), nullable=False, default='default.jpeg')
    date_created = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    mybook= db.relationship('Mybook', backref='author', lazy=True, passive_deletes=True)
    bokitems = db.relationship('Bokitems', backref='author', lazy=True, passive_deletes=True)
    suggestion_contact = db.relationship('Suggestion_Contact', backref='author', lazy=True, passive_deletes=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}, '{self.image_file}')"


    
#     def get_reset_token(self, expires_sec=1800):
#         s = Serializer(app.config['SECRET_KEY'], expires_sec)
#         return s.dumps({'user_id': self.id}).decode('utf-8')

#     @staticmethod
#     def verify_reset_token(token):
#         s = Serializer(app.config['SECRET_KEY'])
#         try:
#             user_id = s.loads(token)['user_id']
#         except:
#             return None
#         return User.query.get(user_id)

    



class Bokitems(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    stb_title = db.Column(db.String(100), nullable=False)
    th_auth = db.Column(db.String(100), nullable=False)
    my_category = db.Column(db.String(100), nullable=False)
    nm_issuerer = db.Column(db.String(100), nullable=False)
    bok_profile = db.Column(db.String(100), nullable=False, default='default.jpg')
    user = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f"Bookitems('{self.stb_title}', '{self.th_auth}', '{self.my_category}', '{self.nm_issuerer}')"



class Mybook(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    the_title = db.Column(db.String(length=100), nullable=False)
    thebook_auth = db.Column(db.String(length=100), nullable=False)
    dpment = db.Column(db.String(length=100), nullable=False)
    date_request = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    user = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f"Mybook(('{self.title}', '{self.contents}', '{self.date_request}')"



class Suggestion_Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=100), nullable=False)
    student_id= db.Column(db.String(length=100), nullable=False)
    subject = db.Column(db.String(length=100), nullable=False)
    phone_number = db.Column(db.String(length=15), nullable=False)
    text_area = db.Column(db.String(length=150), nullable=False)
    user = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f"Suggestion_Contact(('{self.name}', '{self.email}', '{self.subject}','{self.text_area}')"



class AdminSession(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    staffid = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return f"AdminSession('{self.staffid}')"


