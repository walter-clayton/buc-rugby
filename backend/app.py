import os
import uuid
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from testing import TESTS
# from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
# from models import db, InfoModel

# MIGRATION_DIR = os.path.join('models', 'migrations')

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://walter:secure@localhost/mydatabase'
# db.init_app(app)
# migrate = Migrate(app, db, directory=MIGRATION_DIR)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# @app.route('/form')
# def form():
#     return render_template('form.html')

# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'GET':
#         return "Login via the login Form"
     
#     if request.method == 'POST':
#         firstName = request.form['firstName']
#         lastName = request.form['lastName']
#         new_user = InfoModel(firstName=firstName, lastName=lastName)
#         db.session.add(new_user)
#         db.session.commit()
#         return f"Done!!"

# @app.route("/list")
# def list():
#     lists=db.engine.execute("SELECT * FROM info_table order by id")
#     return render_template('list.html',lists=lists)


# def remove_test(test_id):
#     for test in TESTS:
#         if test['id'] == test_id:
#             TESTS.remove(test)
#             return True
#     return False

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
    app.run(debug=True)