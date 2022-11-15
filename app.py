#!flask/bin/python
from flask import Flask
from flask import jsonify
from ovpn import OVPN
import json
from nemiling import Nemiling
# jsonify
# waitress
# flask

# how to open port
# firewall-cmd --zone=public --add-port=80/tcp --permanent
# firewall-cmd --reload

app = Flask(__name__)
vpn = OVPN(r"/usr/local/openvpn_as/scripts/")
payservice = Nemiling()

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/users/check', methods=['GET'])
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

@app.route('/users/check/<int:uid>', methods=['GET'])
def checkUser(uid):
    answer = payservice.checkMember(uid)
    return answer

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=3256)
