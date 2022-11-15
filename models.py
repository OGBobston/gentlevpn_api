from peewee import *

users = SqliteDatabase('users.db')

class User(Model):
    id = PrimaryKeyField(null=False)
    tgid = IntegerField()
    status = IntegerField()

    class Meta:
        database = users
        db_table = "users"
        order_by = ('id',)
