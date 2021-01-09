import os
import uuid
import json, sys
from flask import Flask, jsonify, request, render_template, flash, redirect
from flask_cors import CORS
from testing import TESTS
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db, InfoModel
from psycopg2 import connect, Error
from psycopg2.extras import Json
from psycopg2.extras import json as psycop_json

MIGRATION_DIR = os.path.join('models', 'migrations')

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '4ab17c344aa9779f50807c218a838d17'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://walter:secure@localhost/mydatabase'
db.init_app(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('list'))
    return render_template('form.html', title='Register', form=form)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        new_user = InfoModel(firstName=firstName, lastName=lastName)
        db.session.add(new_user)
        db.session.commit()
        return f"Done!!"

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

if __name__ == '__main__':
    app.run(debug=True)