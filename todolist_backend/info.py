import json
from pathlib import Path


PROJECT_NAME: str = "TodoListBackend"
PROJECT_ROOT: Path = Path(__file__).parents[1].resolve()
PACKAGE_NAME: str = "todolist_backend"
PACKAGE_ROOT: Path = Path(__file__).parents[0].resolve()
CONFIGS_DIR = PROJECT_ROOT / "configs"


DBSERVER_FILENAME = "dbserver.json"
DBSERVER_CONFIGS = json.load((CONFIGS_DIR / DBSERVER_FILENAME).open("r"))
