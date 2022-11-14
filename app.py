#!flask/bin/python
from flask import Flask
import os, subprocess
from flask import jsonify
# jsonify
# waitress
# flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/users/list', methods=['GET'])
def getUsers():
    output = subprocess.check_output([r'cd /usr/local/openvpn_as/scripts/ && ./sacli UserPropGet'], shell=True)
    answer = output
    return answer

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=3256)
