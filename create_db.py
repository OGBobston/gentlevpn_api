from peewee import *
from models import *

if __name__ == '__main__':
    try:
        User.create_table()
    except:
        print("DB create error")
