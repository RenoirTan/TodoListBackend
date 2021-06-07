import json
from pathlib import Path
from typing import *


VERSION: Tuple[int, int, int] = (0, 1, 0)
VERSION_STR: str = "{0}.{1}.{2}".format(*VERSION)


PROJECT_NAME: str = "TodoListBackend"
PROJECT_ROOT: Path = Path(__file__).parents[1].resolve()
PACKAGE_NAME: str = "todolist_backend"
PACKAGE_ROOT: Path = Path(__file__).parents[0].resolve()
CONFIGS_DIR: Path = PROJECT_ROOT / "configs"


DBSERVER_FILENAME: str = "dbserver.json"
DBSERVER_CONFIGS: Dict[str, Any] = json.load(
    (CONFIGS_DIR / DBSERVER_FILENAME).open("r")
)
MONGOENGINE_ALIAS: str = "todolist_dbclient"


FLASKAPP_FILENAME: str = "flaskapp.json"
FLASKAPP_CONFIGS: Dict[str, Any] = json.load(
    (CONFIGS_DIR / FLASKAPP_FILENAME).open("r")
)
