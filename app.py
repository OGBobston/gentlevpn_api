#!flask/bin/python
from flask import Flask
from flask import jsonify
from ovpn import OVPN
import json
from nemiling import Nemiling
from db import UsersDatabase
# jsonify
# waitress
# flask
# requests
# peewee
# mkdir sqlite3 && cd sqlite3
# wget https://www.sqlite.org/2022/sqlite-autoconf-3390400.tar.gz
# cd sqlite-autoconf-3390400 && ./configure && make && make install

# how to open port
# firewall-cmd --zone=public --add-port=80/tcp --permanent
# firewall-cmd --reload

app = Flask(__name__)
vpn = OVPN(r"/usr/local/openvpn_as/scripts/")
payservice = Nemiling()
usersDB = UsersDatabase()

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/users/server', methods=['GET'])
def getUsers():
    answer = json.loads(vpn.getUsersList())
    output = ''
    for key in answer:
        userData = answer[key]
        line = "Логин: " + key + ", тип: " + userData['type']
        if("prop_autologin" in userData):
            if(userData['prop_autologin'] == "true"): line = line + ", автологин"
        if("pvt_password_digest" in userData): line = line + ", установлен пароль"
        output = output + line + "\n"
    return output

@app.route('/users/list', methods=['GET'])
def getUsers():
    answer = usersDB.getAllUsers()
    return answer

@app.route('/users/check/<int:uid>', methods=['GET'])
def checkUser(uid):
    answer = payservice.checkMember(uid)
    return answer

@app.route('/users/add/<int:uid>', methods=['GET'])
def addUser(uid):
    answer = usersDB.addUser(uid)
    return answer

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=3256)
