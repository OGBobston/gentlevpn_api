from peewee import *
from models import *

class UsersDatabase(object):

    def __init__(self):
        try:
            User.create_table()
        except:
            print("DB create error")
