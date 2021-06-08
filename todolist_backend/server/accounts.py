from pathlib import Path
from typing import *
from bson import ObjectId, json_util
from todolist_backend.info import PROJECT_NAME
from todolist_backend.models import Account
from .app_component import AppComponent


BLUEPRINT_NAME: str = Path(__file__).stem
BLUEPRINT_PREFIX: str = "/{0}".format(BLUEPRINT_NAME)


accounts = AppComponent(PROJECT_NAME, BLUEPRINT_NAME)


@accounts.route("/", methods=["GET"])
def root():
    return {"success": True}


@accounts.route("/find_one/<bson_id>", methods=["GET"])
def find_one(bson_id):
    cursor = Account.objects
    print(cursor)
    return "fuck"


@accounts.route("/find_username/one/<username>", methods=["GET"])
def find_username__one(username):
    cursor = Account.objects(username=username)
    print(cursor)
    for account in cursor:
        print(account)
    return "reeeee"
