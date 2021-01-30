# import json, sys
from flask import jsonify, request, render_template, flash, redirect, url_for
from backend import app, db
from .forms import RegistrationForm, LoginForm
from .models import User, Post
from flask_cors import CORS
from .testing import TESTS
import uuid
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, logout_user, login_required

bcrypt = Bcrypt(app)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def remove_test(test_id):
    for test in TESTS:
        if test['id'] == test_id:
            TESTS.remove(test)
            return True
    return False

@app.route('/register', methods = ['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created, you are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@app.route("/list")
def list():
    lists=db.engine.execute("SELECT * FROM info_table order by id")
    return render_template('list.html',lists=lists)

# sanity check route

@app.route('/dashboard', methods=['GET', 'POST'])
def get_tests():
    print(TESTS)
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TESTS.append({
            'id': uuid.uuid4().hex,
            'firstName': post_data.get('firstName'),
            'lastName': post_data.get('lastName')
        })
        response_object['message'] = 'Names added!'
    else:
        response_object['tests'] = TESTS
    return jsonify(response_object)


@app.route('/dashboard/<test_id>', methods=['PUT', 'DELETE'])
def single_test(test_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_test(test_id)
        TESTS.append({
            'id': uuid.uuid4().hex,
            'firstName': post_data.get('firstName'),
            'lastName': post_data.get('lastName')
        })
        response_object['message'] = 'Names updated!'
    if request.method == 'DELETE':
        remove_test(test_id)
        response_object['message'] = 'Name removed!'
    return jsonify(response_object)

@app.route('/alldata', methods=['GET', 'POST'])
def get_allTests():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        new_user = TESTS.append({
            'id': uuid.uuid4().hex,
            'date': post_data.get('date'),
            'firstName': post_data.get('firstName'),
            'lastName': post_data.get('lastName'),
            'bodyFat': post_data.get('bodyFat'),
            'bodyMass': post_data.get('bodyMass'),
            'height': post_data.get('height'),
            'position': post_data.get('position'),
            'tenSprint': post_data.get('tenSprint'),
            'twentySprint': post_data.get('twentySprint'),
        })
        db.session.add(new_user)
        db.session.commit()
        response_object['message'] = 'All DATA added!'
    else:
        response_object['tests'] = TESTS
    return jsonify(response_object)

@app.route('/alldata/<test_id>', methods=['PUT', 'DELETE'])
def all_Tests():
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        TESTS.append({
            'id': uuid.uuid4().hex,
            'date': post_data.get('date'),
            'firstName': post_data.get('firstName'),
            'lastName': post_data.get('lastName'),
            'bodyFat': post_data.get('bodyFat'),
            'bodyMass': post_data.get('bodyMass'),
            'height': post_data.get('height'),
            'position': post_data.get('position'),
            'tenSprint': post_data.get('tenSprint'),
            'twentySprint': post_data.get('twentySprint'),
        })
        response_object['message'] = 'Tests updated!'
    if request.method == 'DELETE':
        remove_test(test_id)
        response_object['message'] = 'Tests removed!'
    return jsonify(response_object)