from waitress import serve
from todolist_backend.server import app, get_configs


def run_debug():
    app.run(**get_configs())


def run_production():
    configs = get_configs()
    configs.pop("debug")
    serve(app, **get_configs())
