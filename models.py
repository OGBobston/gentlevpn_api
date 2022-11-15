from peewee import *

users = SqliteDatabase('users.db')

class User(Model):
    id = PrimaryKeyField(null=False)
    tgid = IntegerField(max_length=50)
    status = IntegerField(max_length=1)

    class Meta:
        database = users
        db_table = "users"
        order_by = ('id',)
