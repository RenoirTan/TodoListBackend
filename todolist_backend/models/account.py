from typing import *
from mongoengine import StringField
from .classes import CommentedODM


class Account(CommentedODM):
    username = StringField(required=True)
    hashdata = StringField(required=True)


Account.setup_odm()
