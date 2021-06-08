from typing import *
from mongoengine import StringField
from mongoengine.fields import DateTimeField, ReferenceField
from .account import Account
from .tagged_odm import TaggedODM


class TodoItem(TaggedODM):
    title = StringField(max_length=60, required=True)
    description = StringField()
    dueDate = DateTimeField()
    account = ReferenceField(Account)


TodoItem.setup_odm()
