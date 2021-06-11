from mongoengine import disconnect
from waitress import serve
from todolist_backend.server import app, get_configs
from .database import panic_init
from .info import MONGOENGINE_ALIAS


def run_debug():
    panic_init()
    app.run(**get_configs())
    # disconnect(alias=MONGOENGINE_ALIAS)


def run_production():
    panic_init()
    configs = get_configs()
    configs.pop("debug")
    serve(app, **configs)
    # disconnect(alias=MONGOENGINE_ALIAS)
