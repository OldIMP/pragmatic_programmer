"""Exercise 11 - YAML to JSON"""

import json
from pathlib import Path
from typing import Final

import yaml

ENCODING: Final[str] = "utf-8"


def main(path):
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
