from tortoise import fields
from app.core.base import Timestamp

class Reservation(Timestamp):
    user = fields.ForeignKeyField("models.User",related_name="user_book")
    room = fields.ForeignKeyField("models.Room",related_name="room_book")
    check_in_date = fields.DatetimeField()
    check_out_date = fields.DatetimeField()
    additional_cost = fields.FloatField(default=0)
    speacial = fields.CharField(max_length=200)