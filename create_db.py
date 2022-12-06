from peewee import *
from models import *

if __name__ == '__main__':
    try:
        users.close()
        User.create_table()
        users.connect()
        print("ok")
    except Exception as e:
        print(e)
