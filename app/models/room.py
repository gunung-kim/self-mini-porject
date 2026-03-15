from tortoise import fields
from app.core.base import RoomType,RoomView,Timestamp

class Room(Timestamp):

    number = fields.CharField(max_length=20,unique=True)
    type = fields.CharEnumField(RoomType)
    view = fields.CharEnumField(RoomView)
    condition = fields.BooleanField(default=True)

    class Meta:
        table = "rooms"