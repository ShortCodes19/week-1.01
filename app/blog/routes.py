from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from app.forms import BlogForm
from app.models import Blog, db

blog = Blueprint('blog', __name__)

@blog.route('/')
@blog.route('/home')
def home():
    posts = Blog.query.all()
    return render_template('home.html', posts=posts)

@blog.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = BlogForm()
    if form.validate_on_submit():
        post = Blog(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.home'))
    return render_template('create.html', form=form)