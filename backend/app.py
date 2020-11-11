import os
import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
from testing import TESTS
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import Test

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://walter:secure@localhost/mydatabase'
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

admin = Admin(app)

admin.add_view(ModelView(Test, db.session))

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def remove_test(test_id):
    for test in TESTS:
        if test['id'] == test_id:
            TESTS.remove(test)
            return True
    return False

# sanity check route
@app.route('/dashboard', methods=['GET', 'POST'])
def get_tests():
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

@app.route('/<test_id>', methods=['PUT', 'DELETE'])
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

if __name__ == '__main__':
    app.run()