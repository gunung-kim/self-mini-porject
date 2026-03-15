from tortoise import fields,models
from datetime import datetime
from enum import Enum

class Timestamp(models.Model):
    id = fields.IntField(pk=True)
    create_at = fields.DatetimeField(auto_now_add=True)
    update_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True

# room Enum class
class RoomType(str,Enum):
    double = "double"
    twin = "twin"
    famliy = "family"

class RoomView(str,Enum):
    ocean = "ocean"
    city = "city"
    wheel = "wheel"

class RoomCondition(str,Enum):
    good = "reservation available"
    Bad = "had reservation"

# cost enum class
class PayWay(str,Enum):
    card = "Card"
    cash = "Cash"
    bank_accoount = "Bank_Account"


