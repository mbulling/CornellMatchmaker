from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Academics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courses = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    delimiter = db.Column(db.String(1))
    notes = db.relationship('Note')
    school = db.Column(db.String(150))
    identity = db.Column(db.String(1))
    type = db.Column(db.String(1))
    partner = db.Column(db.String(1))
    intro = db.Column(db.String(1))
    age = db.Column(db.String(1))
