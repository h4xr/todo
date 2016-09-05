from flask import Flask, jsonify, make_response
import requests
import os
import simplejson as json

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print database_path

with open("{}/database/users.json".format(database_path), "r") as f:
    usr = json.load(f)

@app.route("/", methods=['GET'])
def hello():
    ''' Greet the user '''

    return "Hey! The service is up, how about doing something useful"

@app.route('/users', methods=['GET'])
def users():
    ''' Returns the list of users '''

    resp = make_response(json.dumps(usr, sort_keys=True, indent=4))
    resp.headers['Content-Type']="application/json"
    return resp

@app.route('/users/<username>', methods=['GET'])
def user_data(username):
    ''' Returns info about a specific user '''

    if username not in usr:
        return "Not found"

    return jsonify(usr[username])

@app.route('/users/<username>/lists', methods=['GET'])
def user_lists(username):
    ''' Get lists based on username '''

    try:
        req = requests.get("http://127.0.0.1:5001/lists/{}".format(username))
    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return req.text

if __name__ == '__main__':
    app.run(port=5000, debug=True)
