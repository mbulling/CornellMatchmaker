from flask import Blueprint, render_template, request, flash, redirect, url_for, send_file
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/admin', methods=['GET', 'POST'])
@login_required
def downloadFile():
    admin = "admin@cornell.edu"
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password) and user.email == admin:
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                path = "database.db"
                return send_file(path, as_attachment=True)
            else:
                flash('fuck off.', category='error')
        else:
            flash('fuck off.', category='error')

    return render_template("login.html", user=current_user)
    

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        delimiter = '-'
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        school = request.form.get('school')
        identity = request.form.get('identity')
        type = request.form.get('type')
        partner = request.form.get('partner')
        intro = request.form.get('intro')
        age = request.form.get('age')
        greek = request.form.get('greek')
        doors = request.form.get('doors')
        read = request.form.get('read')
        sports = request.form.get('sports')
        drink = request.form.get('drink')
        smoke = request.form.get('smoke')
        vegan = request.form.get('vegan')
        study = request.form.get('study')
        fish = request.form.get('fish')
        party = request.form.get('party')
        god = request.form.get('god')
        animal = request.form.get('animal')
        country = request.form.get('country')
        music = request.form.get('music')
        pres = request.form.get('pres')
        cook = request.form.get('cook')
        time = request.form.get('time')


        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, delimiter=delimiter, password=generate_password_hash(
                password1, method='sha256'), school=school, identity=identity, type=type, partner=partner, intro=intro, age=age, greek=greek,
                doors=doors, read=read, sports=sports, drink=drink, smoke=smoke, vegan=vegan, study=study, fish=fish, party=party,
                god=god, animal=animal, country=country, music=music, pres=pres, cook=cook, time=time)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
