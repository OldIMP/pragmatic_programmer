"""Exercise 11 - YAML to JSON"""

import json
import sys
from pathlib import Path
from typing import Final

import yaml

ENCODING: Final[str] = "utf-8"


def yaml_2_csv(path):
    """Transform all YAMLs in the specified path to JSONs"""

    for y in Path(path).rglob("*.yaml"):
        with (
            open(y, encoding=ENCODING) as yaml_reader,
            open(y.with_suffix(".json"), "w", encoding=ENCODING) as json_writer,
        ):
            json.dump(
                yaml.safe_load(yaml_reader),
                json_writer,
                indent=4,
                # necessary for date
                default=str,
            )


if __name__ == "__main__":
    arg_len = len(sys.argv)
    if arg_len < 2:
        path_arg = Path.cwd()
    elif arg_len == 2:
        path_arg = Path(sys.argv[1])
    else:
        raise IndexError("Too many arguments were provided, only 1 Path is expected.")

    yaml_2_csv(path_arg)
