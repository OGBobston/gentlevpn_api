from peewee import *
from models import *

class UsersDatabase(object):

    def __init__(self):
        try:
            users.connect()
            User.create_table()
        except Exception as e:
            print(e)

    def addUser(self, id):
        try:
            user = User.get(User.tgid == id).select()
        # except models.UserDoesNotExist:
            # return "Пользователь " + str(id) + " уже существует."

            user = User(
                tgid=id,
                status=0
            )
            ret = user.save()
            return ret
        except Exception as e:
            print(e)
            return 0

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
