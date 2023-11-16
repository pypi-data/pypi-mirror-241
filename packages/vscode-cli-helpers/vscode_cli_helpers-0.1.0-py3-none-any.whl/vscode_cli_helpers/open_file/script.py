#! /usr/bin/env python3

import logging
import os
import subprocess
from pathlib import Path

import click

from vscode_cli_helpers.open_file.config_reader import ConfigReader


def find_code_workspace(dir_: Path) -> str:
    """Find the VSCode workspace for the given path."""
    workspaces = list(dir_.glob("*.code-workspace"))
    if len(workspaces) == 1:
        return Path(workspaces[0]).name
    else:
        return "."


def add_extension(name: str) -> str:
    """Add the .py extension if it is missing."""
    if "." not in name:
        return name + ".py"
    else:
        return name


@click.command()
@click.argument("path", type=str, default="t")
def main(path: str) -> None:
    """``vscode-cli-helper-new-python-script`` is a command line tool for opening a new or existing
    Python script in VSCode and navigating to a specific line. If the file does not exist,
    it will be created and made executable. Then a template will be written to the file before
    opening it in VS Code.

    EXAMPLES

    .. code-block:: bash

      $ vscode-cli-helper-new-python-script a.py

    Opens ``a.py`` in VS Code and navigates to line 1. If ``a.py`` does not exist, it will be created
    and made executable. Then a template will be written to the file before opening it in VS Code. ::

      vscode-cli-helper-new-python-script a

    If ``a`` exists, opens it in VS Code and navigates to line 1. If ``a`` does not exist,
    ``a.py`` will be created and made executable. Then a template will be written to the file
    before opening it in VSCode. ::

      vscode-cli-helper-new-python-script a:10
      vscode-cli-helper-new-python-script a.py:10

    Sames as above but also navigates to line 10
    """
    logging.basicConfig(level=logging.INFO)
    config = ConfigReader()
    filename = Path(path).name
    dir_ = Path(path).parent
    (basename, line_no) = filename.split(":") if ":" in filename else (filename, None)
    if basename is not None:
        filename = add_extension(basename)
    workspace = find_code_workspace(dir_)
    path2 = Path(dir_) / filename
    if not path2.exists():
        with open(path2, "w", encoding="utf-8") as f:
            f.write(config.get_template("python"))
        logging.info(f"Creating file: {path2}")
        os.chmod(path2, 0o755)
    else:
        logging.info(f"File exists: {path}")
    if line_no is not None:
        filename = f"{filename}:{line_no}"
    cmd = ["code", "-g", filename, workspace]
    logging.info(f"Running: {cmd} in directory: {dir_}, workspace: {workspace}")
    subprocess.Popen(cmd, cwd=dir_, start_new_session=True)


if __name__ == "__main__":  # pragma: no cover
    main()
