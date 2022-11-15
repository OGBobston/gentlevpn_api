from peewee import *
from models import *


class UsersDatabase(object):

    def __init__(self):
        users = SqliteDatabase('users.db', pragmas={
            'journal_mode': 'wal',
            'cache_size': -1024 * 64})
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

    def getAllUsers():
        return User.select()
