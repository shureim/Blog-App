from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort,flash
from ..models import User,Blog,Subscriber,Comment,Role
from .forms import UpdateProfile,BlogForm,SubscriberForm,CommentForm
from .. import db,photos
from . import main
from flask import Flask
from ..email import mail_message

# import markdown2

@main.route('/',methods = ['GET','POST'])
def index():

    blogs= Blog.query.all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/welcome_subscriber",new_subscriber.email,subscriber=new_subscriber)


    title = "My blog page"

    return render_template('index.html', blogs = blogs, title=title,subscriber_form = form)

@main.route('/new_blog', methods = ['GET','POST'])
@login_required
def newblog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        blog= form.blog.data

        #Updated blog instance
        new_blog= Blog(title = title, blog = blog)

        #save blog instance
        new_blog.save_blog()
        subscriber = Subscriber.query.all()
        for subscriber in subscribers:

            mail_message("New Blog ","email/new_blog",subscriber.email,blog=new_blog)


        return redirect(url_for('main.index'))

    title = "View blog's"
    return render_template('new_blog.html',title = title, blog_form = form)


@main.route("/post/<int:id>",methods=['GET','POST'])
def blog(id):
    blog=blog.query.get_or_404(id)
    comment = Comment.query.all()
    form=CommentForm()

    db.session.add(blog)
    db.session.commit()

    if form.validate_on_submit():
        comment=form.comment.data
        new_comment = Comment(id=id,comment=comment,user_id=current_user.id,blog_id=blog.id)

        new_comment.save_comment()

        return redirect("/blog/{blog_id}".format(blog_id=blog.id))

    return render_template('blog.html',blog=blog,comments=comment,comment_form=form)




@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    title = "View your profile"

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, title=title)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():

        comment_content = form.comment.data

        comment = Comment(comment_content= comment_content,blog_id=id)

        db.session.add(comment)
        db.session.commit()

    comment = Comment.query.filter_by(blog_id=id).all()

    return render_template('index.html', title='New Comment', comment=comment,comment_form=form)

@main.route('/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete(id):
    delete_blog = Blog.query.filter_by(id=id).first()
    db.session.delete(delete_blog)
    db.session.commit()

    return redirect(url_for('main.index'))

    # return render_template('index.html')


@main.route('/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete_comment(id):
    delete_comment = Comment.query.filter_by(id=id).first()
    db.session.delete(delete_comment)
    db.session.commit()

    return redirect(url_for('main.index'))

    return render_template('index.html')
