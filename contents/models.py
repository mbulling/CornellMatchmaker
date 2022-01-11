from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


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
    school = db.Column(db.String(150))
    identity = db.Column(db.String(1))
    type = db.Column(db.String(1))
    partner = db.Column(db.String(1))
    intro = db.Column(db.String(1))
    age = db.Column(db.String(1))
    greek = db.Column(db.String(1))
    doors = db.Column(db.String(1))
    read = db.Column(db.String(1))
    sports = db.Column(db.String(1))
    drink = db.Column(db.String(1))
    smoke = db.Column(db.String(1))
    vegan = db.Column(db.String(1))
    study = db.Column(db.String(1))
    fish = db.Column(db.String(1))
    mac = db.Column(db.String(1))
    party = db.Column(db.String(1))
    god = db.Column(db.String(1))
    animal = db.Column(db.String(1))
    country = db.Column(db.String(1))
