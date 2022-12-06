from peewee import *
from models import *

class UsersDatabase(object):

    def __init__(self):
        try:
            User.create_table()
            users.connect()
        except:
            print("DB connect error")

    def addUser(self, id):
        try:
            user = User.get(User.tgid == id).select()
        # except models.UserDoesNotExist:
        except Exception as e:
            # return "Пользователь " + str(id) + " уже существует."
            return e

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
        try:
            return User.select()
        except Exception as e:
            print(e)

    def setStatusPayed(self, id):
        try:
            user = User.get(User.tgid == id)
            user.status = 1
        except Exception as e:
            print(e)

    def setStatusNotPayed(self, id):
        try:
            user = User.get(User.tgid == id)
            user.status = 0
        except Exception as e:
            print(e)
