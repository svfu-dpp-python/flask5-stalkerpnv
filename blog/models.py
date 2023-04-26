from hashlib import scrypt
from os import urandom
from base64 import b64encode, b64decode

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin

db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()


@login.user_loader
def load_user(user_id):
    return User.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    hash = db.Column(db.String(), nullable=False)
    salt = db.Column(db.String(48), nullable=False)
    name = db.Column(db.String(75), nullable=False)

    def __str__(self):
        return f"{self.name}"

    def set_password(self, password):
        n, r, p = 16384, 8, 1
        salt = urandom(24)
        self.salt = f"{b64encode(salt).decode()} {n} {r} {p}"
        self.hash = scrypt(password.encode(), salt=salt, n=n, r=r, p=p)

    def check_password(self, password):
        salt, n, r, p = self.salt.split()
        salt = b64decode(salt.encode())
        n, r, p = int(n), int(r), int(p)
        return self.hash == scrypt(password.encode(), salt=salt, n=n, r=r, p=p)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(75), nullable=False)
    text = db.Column(db.Text)
    published = db.Column(db.DateTime, nullable=False)

    def __str__(self):
        return self.title
