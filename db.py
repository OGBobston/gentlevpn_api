from peewee import *
from models import *

class UsersDatabase(object):

    def __init__(self):
        try:
            users.connect()
            # User.create_table()
        except:
            print("DB connect error")

    def addUser(self, id):
        try:
            user = User.get(User.tgid == id).select()
        except models.UserDoesNotExist:
            return "Пользователь " + str(id) + " уже существует."

        user = User(
            tgid=id,
            status=0
        )
        ret = user.save()
        return ret

    def deleteUser(self, id):
        try:
            user = User.get(User.tgid == id)
            ret = user.delete_instance()
            return ret
        except:
            return 0

    def getAllUsers(self):
        return User.select()

    def setStatusPayed(self, id):
        user = User.get(User.tgid == id)
        user.status = 1

    def setStatusNotPayed(self, id):
        user = User.get(User.tgid == id)
        user.status = 0
