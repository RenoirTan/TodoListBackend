from typing import *
from flask import Flask
from todolist_backend.info import PROJECT_NAME, FLASKAPP_CONFIGS


app = Flask(PROJECT_NAME)
app.secret_key = FLASKAPP_CONFIGS["secretkey"]


def get_configs() -> Dict[str, Any]:
    return FLASKAPP_CONFIGS["options"].copy()
