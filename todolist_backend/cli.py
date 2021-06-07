from waitress import serve
from todolist_backend.server import app, get_configs
from .database import panic_init


def run_debug():
    panic_init()
    app.run(**get_configs())


def run_production():
    panic_init()
    configs = get_configs()
    configs.pop("debug")
    serve(app, **configs)
