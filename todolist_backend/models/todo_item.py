from typing import *
from mongoengine import StringField
from mongoengine.fields import DateTimeField
from .tagged_odm import TaggedODM


class TodoItem(TaggedODM):
    title = StringField(max_length=60, required=True)
    description = StringField()
    dueDate = DateTimeField()


TodoItem.setup_odm()
