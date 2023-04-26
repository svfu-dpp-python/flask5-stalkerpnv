from flask import Flask

from .admin import admin
from .models import db, login, migrate
from . import views


def create_app():
    app = Flask(__name__)

    # Конфигурация
    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

    # Расширения
    db.init_app(app)
    login.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    # Функции представления
    app.add_url_rule("/", view_func=views.index_page)
    app.add_url_rule("/post/<int:post_id>/", view_func=views.post_page, methods=["GET", "POST"])
    app.add_url_rule("/login/", view_func=views.login_page, methods=["GET", "POST"])
    app.add_url_rule("/logout/", view_func=views.logout)

    return app
