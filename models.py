from peewee import *

class BaseModel(Model):
    class Meta:
        database = users


class User(BaseModel):
    id = PrimaryKeyField(null=False)
    tgid = IntegerField(max_length=50)
    status = IntegerField(max_length=1)

    class Meta:
        db_table = "users"
        order_by = ('id',)
