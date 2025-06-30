from tortoise import Model, fields
from datetime import datetime

class User(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=300)

    class Meta:
        ordering=["name"]