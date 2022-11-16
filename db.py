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
        user = User(
            tgid=id,
            status=0
        )
        user.save()

    def deleteUser(self, id):
        user = User.get(User.tgid == id)
        user.delete_instance()

    def getAllUsers(self):
        return User.select()

    def setStatusPayed(self, id):
        user = User.get(User.tgid == id)
        user.status = 1

    def setStatusNotPayed(self, id):
        user = User.get(User.tgid == id)
        user.status = 0
