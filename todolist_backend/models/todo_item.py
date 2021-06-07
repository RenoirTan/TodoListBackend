from typing import *
from mongoengine import StringField
from mongoengine.fields import DateTimeField
from .classes import TaggedODM


class TodoItem(TaggedODM):
    title = StringField(max_length=60, required=True)
    description = StringField()
    dueDate = DateTimeField()


TodoItem.setup_odm()
