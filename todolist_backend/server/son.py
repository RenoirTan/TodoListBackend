from functools import reduce
from typing import *
from bson import BSON, json_util
import json
from mongoengine.document import Document


def merge(*objects: Dict) -> Dict:
    """
    Merge multiple dictionary-like objects together.
    """
    # Merge ItemsView iterators
    iterator = reduce(lambda a, b: a | b.items(), objects, dict().items())
    return dict(iterator)
