from peewee import *

DATABASE_NAME = "ovpn"
USER  = "ovpn"
PASSWORD = "RawPY7DjZdiW8hD7"
connection = MySQLDatabase(DATABASE_NAME,
                         user=USER, password=PASSWORD)

class User(Model):
    id = PrimaryKeyField(null=False)
    tgid = IntegerField(unique=True)
    status = IntegerField()

    class Meta:
        database = connection
        db_table = "users"
        order_by = ('id',)
