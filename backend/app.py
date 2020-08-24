import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
from testing import TESTS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def remove_test(test_id):
    for test in TESTS:
        if test['id'] == test_id:
            TESTS.remove(test)
            return True
    return False

# sanity check route
@app.route('/', methods=['GET', 'POST'])
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