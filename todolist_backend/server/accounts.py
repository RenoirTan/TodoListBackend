from pathlib import Path
from typing import *
from todolist_backend.info import PROJECT_NAME
from .app_component import AppComponent


BLUEPRINT_NAME: str = Path(__file__).stem
BLUEPRINT_PREFIX: str = "/{0}".format(BLUEPRINT_NAME)


accounts = AppComponent(PROJECT_NAME, BLUEPRINT_NAME)


@accounts.route("/", methods=["GET"])
def root():
    return {"success": True}
