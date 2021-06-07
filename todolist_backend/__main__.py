from difflib import get_close_matches
from typing import *
import sys
from todolist_backend import cli


def get_subcommand(subcommand: str, possibilities: List[str]) -> str:
    try:
        return get_close_matches(subcommand, possibilities, 1, 0.2)[0]
    except IndexError as e:
        raise ValueError("Bad subcommand: {0}".format(subcommand)) from e


handlers = {
    "debug": cli.run_debug,
    "production": cli.run_production
}


def main(args: List[str]) -> int:
    subcommand = get_subcommand(args[1], list(handlers.keys()))
    print("Running in {0} mode...".format(subcommand))
    handlers[subcommand]()
    return 0


def run() -> int:
    return main(sys.argv)


if __name__ == "__main__":
    sys.exit(run())
