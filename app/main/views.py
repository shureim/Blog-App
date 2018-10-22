# from flask_login import login_required,current_user
# from flask import render_template,request,redirect,url_for,abort,flash
# from ..models import User,Blog
# from .forms import UpdateProfile,BlogForm
# from .. import db,photos
# from . import main
# from flask import Flask
#
# # import markdown2
#
# @main.route('/')
# def index():
#
#     blogs = Blog.query.all()
#
#     title = "Home page"
#
#     return render_template('index.html', blogs = blogs, title=title)
#
# @main.route('/blog/new', methods = ['GET','POST'])
# @login_required
# def new_blog():
#     form = BlogForm()
#     if form.validate_on_submit():
#         title = form.title.data
#         blog= form.blog.data
#
#         #Updated blog instance
#         blog= Blog(title = title, user = current_user)
#
#         #save blog instance
#         blog.save_blog()
#         return redirect(url_for('main.index'))
#
#     title = "View blog's"
#     return render_template('new_blog.html',title = title, blog_form = form)
#
#
# @main.route('/user/<uname>')
# def profile(uname):
#     user = User.query.filter_by(username = uname).first()
#
#     title = "View your profile"
#
#     if user is None:
#         abort(404)
#
#     return render_template("profile/profile.html", user = user, title=title)
#
# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)
#
#     form = UpdateProfile()
#
#     if form.validate_on_submit():
#         user.bio = form.bio.data
#
#         db.session.add(user)
#         db.session.commit()
#
#         return redirect(url_for('.profile',uname=user.username))
#
#     return render_template('profile/update.html',form =form)
#
# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))
