# from werkzeug.security import generate_password_hash,check_password_hash
# from . import db, login_manager
# from flask_login import UserMixin
# from datetime import datetime
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
#
#
# class User(UserMixin,db.Model):
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255),index = True)
#     email = db.Column(db.String(255),unique = True,index = True)
#     bio = db.Column(db.String(255))
#     profile_pic_path = db.Column(db.String())
#     pass_secure = db.Column(db.String(255))
#     role_id = db.Column(db.Integer,db.ForeignKey("roles.id"))
#
#
#
#
#     @property
#     def password(self):
#         raise AttributeError('You cannot read the password attribute')
#
#     @password.setter
#     def password(self, password):
#         self.pass_secure = generate_password_hash(password)
#
#
#     def verify_password(self,password):
#         return check_password_hash(self.pass_secure,password)
#
#     def __repr__(self):
#         return f'User {self.username}'
#
# class Subscriber(db.Model):
#     __tablename__='subscribers'
#
#     id=db.Column(db.Integer,primary_key=True)
#     email = db.Column(db.String(255),unique=True,index=True)
#
#     def save_subscriber(self):
#         db.session.add(self)
#         db.session.commit()
#
# class Blog(db.Model):
#
#     __tablename__ = 'blogs'
#
#     id = db.Column(db.Integer,primary_key=True)
#     blog_id = db.Column(db.Integer)
#     title = db.Column(db.String(255))
#     blog = db.Column(db.String)
#     posted = db.Column(db.DateTime,default=datetime.utcnow)
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
#
#
#     def save_blog(self):
#         db.session.add(self)
#         db.session.commit()
#
#     @classmethod
#     def get_blog(cls, id):
#         blogs = Blog.query.all()
#         return blogs
#
#         # @classmethod
#         # def get_all_blogs(cls):
#         #     blogs = Blog.query.filter_by(id).all()
#         #     return blogs
#
# class Comment(db.Model):
#     __tablename__='comments'
#
#     id = db.Column(db.Integer,primary_key = True)
#     comment = db.Column(db.String)
#     posted = db.Column(db.DateTime,default=datetime.utcnow)
#     blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
#
#     def save_comment(self):
#         db.session.add(self)
#         db.session.commit()
#
#     def delete_comment(self):
#         db.session.delete(self)
#         db.session.commit()
#
# class Role(db.Model):
#     __tablename__ = 'roles'
#
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(255))
#     users= db.relationship('User',backref='role',lazy="dynamic")
#
#     def __repr__(self):
#         return f'User{self.name}'
