from tortoise import fields
from app.core.base import Timestamp,PayWay

class User(Timestamp):
    username = fields.CharField(max_length=100)
    password = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255,unique=True)
    phone_num = fields.CharField(null=True,max_length=100,default=None)
    payway = fields.CharEnumField(PayWay)
    is_admin = fields.BooleanField(default=False)

    class Meta:
        table = "users"