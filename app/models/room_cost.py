from tortoise import fields
from app.models.room import Timestamp

class RoomCost(Timestamp):
    room = fields.ForeignKeyField("models.Room",related_name="costs")
    cost_plan = fields.CharField(max_length=50)
    cost = fields.IntField()
    discount = fields.FloatField(default=0.0)

    class Meta:
        table="room_costs"