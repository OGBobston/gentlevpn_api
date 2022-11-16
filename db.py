from peewee import *
from models import *

class UsersDatabase(object):

    def __init__(self):
        try:
            users.connect()
            User.create_table()
        except peewee.InternalError as px:
            print(str(px))

    def addUser(self, id):
        user = User(
            tgid=id,
            status=0
        )
        user.save()

    def deleteUser(self, id):
        user = User.get(Category.tgid == id)
        user.delete_instance()

    def getAllUsers(self):
        return User.select()
