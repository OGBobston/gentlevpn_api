from peewee import *
from models import *

if __name__ == '__main__':
    try:
    	if not users.is_closed():
    		users.close()
        User.create_table()
        print("ok")
    except Exception as e:
        print(e)
