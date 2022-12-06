from peewee import *
from models import *

class UsersDatabase(object):

    def __init__(self):
        try:
            users.connect()
        except Exception as e:
            print(e)

    def addUser(self, id):
        try:
            user = User.get(User.tgid == id).select()
            print(str(user))
            user = User.get(User.tgid == id)
            print(str(user))
        except User.DoesNotExist:
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
            return User.select().execute()
        except Exception as e:
            print(e)

    def setStatusPayed(self, id):
        try:
            user = User.get(User.tgid == id)
            user.status = 1
            user.save()
        except Exception as e:
            print(e)

    def setStatusNotPayed(self, id):
        try:
            user = User.get(User.tgid == id)
            user.status = 0
            user.save()
        except Exception as e:
            print(e)
