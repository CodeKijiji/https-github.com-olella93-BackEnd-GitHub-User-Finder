from server.extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password_hash = db.Column("password_hash", db.String(255), nullable=False)

    bookmarks = db.relationship('Item', backref='owner', cascade="all, delete-orphan")
    comments = db.relationship('Comment', backref='author', cascade="all, delete-orphan")

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"

    @validates("email")
    def validate_email(self, key, email):
        if "@" not in email:
            raise ValueError("Invalid email format")
        return email
