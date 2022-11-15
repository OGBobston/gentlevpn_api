#!flask/bin/python
from flask import Flask
from flask import jsonify
from ovpn import OVPN
# jsonify
# waitress
# flask

# how to open port
# firewall-cmd --zone=public --add-port=80/tcp --permanent
# firewall-cmd --reload

app = Flask(__name__)
vpn = OVPN(r"/usr/local/openvpn_as/scripts/")

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/users/list', methods=['GET'])
def getUsers():
    answer = vpn.getUsersList()
    print(answer)
    return answer

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=3256)
