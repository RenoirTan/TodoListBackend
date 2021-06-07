from typing import *
from flask import Flask, Blueprint


class AppComponent(Blueprint):
    def __init__(self, app: str, name: str, *args, **kwargs):
        super().__init__(name, app, *args, **kwargs)

    def route(self, rule: str, *args, **kwargs) -> Callable:
        return super().route(self._get_route(rule), *args, **kwargs)

    
    def _get_route(self, rule: str) -> str:
        route = "/" + self.name
        if rule[0:] != "/":
            route += "/"
        route += rule
        return route
