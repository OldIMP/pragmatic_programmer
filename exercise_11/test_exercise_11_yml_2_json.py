# pylint: disable=missing-docstring
import json
import shutil
from datetime import datetime
from pathlib import Path

import yaml

from exercise_11_yml_2_json import ENCODING, main


def test(request, tmp_path):
    shutil.copytree(request.path.parent / "test_data", tmp_path, dirs_exist_ok=True)

    main(tmp_path)

    jsons_yamls = (sorted(Path(tmp_path).rglob(f"*.{t}")) for t in ("json", "yaml"))
    for j, y in zip(*jsons_yamls, strict=True):
        with (
            open(j, encoding=ENCODING) as json_reader,
            open(y, encoding=ENCODING) as yaml_reader,
        ):
            actual = json.load(json_reader, object_hook=parse_date)
            assert actual == yaml.safe_load(yaml_reader)


def parse_date(obj):
    for k, v in obj.items():
        if k == "date":
            obj[k] = datetime.fromisoformat(v).date()

    return obj
