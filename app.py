#!flask/bin/python
from flask import Flask
from flask import jsonify, make_response, send_file
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
# tar xvfz sqlite-autoconf-3390400.tar.gz
# cd sqlite-autoconf-3390400 && ./configure && make && make install
# sqlite3 users

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
def getUsersFromServer():
    try:
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
    except Exception as e:
        ret = "Ошибка запроса данных."
        print(e)

@app.route('/users/list', methods=['GET'])
def getUsers():
    try:
        answer = usersDB.getAllUsers()
        users_data = []
        users_data_text = ''
        for user in answer:
            users_data.append({
                'id': user.id,
                'tgid': user.tgid,
                'status': user.status
            })
            payed = ", подписка не оплачена"
            if(user.status == 1): payed = ", подписка оплачена"
            line = "ID: " + str(user.id) + ", tgid: " + str(user.tgid) + payed + " : status= " + str(user.status)
            users_data_text = users_data_text + line + "\n"
    except Exception as e:
        users_data_text = "Ошибка запроса данных."
        print(e)
    return users_data_text

@app.route('/users/check/<int:uid>', methods=['GET'])
def checkUser(uid):
    ret = "Ошибка"
    try:
        answer = payservice.checkMember(uid)
        answer = json.loads(answer)
        payserviceData = {}

        if(answer['status'] == "ok"):
            payserviceData = answer['message']

        if(payserviceData['active'] == "1"):
            answerDB = usersDB.setStatusPayed(uid)
            ret = "Подписка активна до " + str(payserviceData['end_date']) + "."
            vpn.register(uid)
        else:
            answerDB = usersDB.setStatusNotPayed(uid)
            ret = "Подписка не оплачена."
            vpn.deleteUser(uid)
    except Exception as e:
        ret = "Ошибка запроса данных."
        print(e)

    return ret

@app.route('/users/add/<int:uid>', methods=['GET'])
def addUser(uid):
    try:
        answer = usersDB.addUser(uid)
        checkUser(uid)
        if(answer == 1): ret = "Вы успешно зарегистрировались!"
        else: ret = "Что-то пошло не так."
    except Exception as e:
        ret = "Ошибка запроса данных."
        print(e)
    return ret

@app.route('/users/remove/<int:uid>', methods=['GET'])
def removeUser(uid):
    try:
        answer = usersDB.deleteUser(uid)
        ret = "Ошибка"
        if(answer == 1): ret = "Успешно"
        else: ret = "Что-то пошло не так."
        vpn.deleteUser(uid)
    except Exception as e:
        ret = "Ошибка запроса данных."
        print(e)
    return ret


@app.route('/certificate/get/<int:uid>', methods=['GET'])
def getCertificate(uid):
    try:
        file = vpn.getCertificate(uid)
    except Exception as e:
        file = "Ошибка запроса данных."
        print(e)
    return send_file(file)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=3256)
