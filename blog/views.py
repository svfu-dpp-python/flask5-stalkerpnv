from flask import abort, flash, render_template, redirect, request, session, url_for

from .models import db, User, Post, Comment
from .forms import LoginForm, CommentForm
from datetime import datetime


def index_page():
    query = db.select(Post).order_by(Post.published.desc())
    posts = db.session.execute(query).scalars()
    return render_template("index.html", posts=posts)


def post_page(post_id):
    post = db.get_or_404(Post, post_id)
    form = CommentForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # Создать объект класса Comment
            comment = Comment()
            comment.text = form.text.data
            comment.username = form.username.data
            comment.post = post
            comment.published = datetime.now()
            db.session.add(comment)
            db.session.commit()
            return redirect(url_for("post_page", post_id=post_id))
    return render_template("post.html", post=post, form=form)


def login_page():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            query = db.select(User).filter(username=form.username.data)
            users = db.session.execute(query).scalars()
            if len(users) == 1:
                user = next(iter(users))
                if user.check_password(form.password.data):
                    session["user_id"] = user.id
                    session["username"] = user.name
                    next_url = request.args.get("next")
                    return redirect(next_url or url_for("index_page"))
                else:
                    flash("Неправильный логин или пароль")
            else:
                flash("Неправильный логин или пароль")
        else:
            flash("Неправильный логин или пароль")
    return render_template("login.html", form=form)


def logout():
    session.pop("user_id")
    session.pop("username")
    return redirect(url_for("index_page"))
