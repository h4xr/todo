from flask import Flask, jsonify, make_response
import json
import requests
import os
import subprocess

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

with open('{}/database/todo.json'.format(database_path), "r") as jsf:
    todo_list = json.load(jsf)

@app.route('/', methods=['GET'])
def hello():
    ''' Greet the user '''

    return "Todo service is up"

@app.route('/lists', methods=['GET'])
def show_lists():
    ''' Displays all the lists '''

    tlists = []
    for username in todo_list:
        for lname in todo_list[username]:
            tlists.append(lname)
    return jsonify(lists=tlists)

@app.route('/lists/<username>', methods=['GET'])
def user_list(username):
    ''' Returns a user oriented list '''

    if username not in todo_list:
        return "No list found"

    return jsonify(todo_list[username])

# Lets add a nice way to catalog service pids and kill them
@app.route('/svcpslist', methods=['GET'])
def ps_list():
    ''' Returns a list of processes '''

    pslist = {}
    proc = subprocess.Popen(['pgrep', '-a', 'python'],stdout=subprocess.PIPE)
    while True:
      line = proc.stdout.readline()
      if not line:
        break
      pid, _, name = line.split()
      pslist[pid] = { "pid": pid, "name": name }
    return jsonify(pslist)

@app.route('/stopsvc', methods=['GET'])
def stopsvc():
    ''' Stops all svc processes '''

    procs = json.loads(ps_list().get_data())
    print "Killing the following processes:"
    for proc in procs:
        print "'{} - {}' ".format(proc, procs[proc]["name"])
    output = subprocess.check_output(['pkill', 'python'])
    # We will never get here
    return jsonify('{"Status": "Stopped"}')


if __name__ == '__main__':
    app.run(port=5001, debug=True)
