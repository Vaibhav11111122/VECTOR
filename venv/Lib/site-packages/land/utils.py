#!/usr/bin/env python
import json
import inspect
import pathlib
import textwrap
import subprocess

import rich
import rich.traceback

rich.traceback.install(show_locals=True)


def find_file_name(name):
    cwd = pathlib.Path.cwd()
    for child in cwd.iterdir():
        if child.name == name:
            return child


def commit(system):
    for path, value in system.items():
        if path.endswith(".json"):
            value = json.dumps(value)

        if isinstance(value, str):
            if value.startswith("\n"):
                value = value[1:]

            if value.endswith("\n"):
                value = value[:-1]

            value = textwrap.dedent(value)

        path = pathlib.Path(path)

        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w+") as f:
            f.write(value)


def dispatch(fn, *args):
    directive = fn(*args)

    if inspect.isgeneratorfunction(fn):
        for command in directive:
            result = subprocess.run(command, shell=True, check=False)
            try:
                directive.send(result)
            except StopIteration:
                pass
    elif isinstance(directive, dict):
        commit(directive)
    else:
        print("default")
        print(directive)
