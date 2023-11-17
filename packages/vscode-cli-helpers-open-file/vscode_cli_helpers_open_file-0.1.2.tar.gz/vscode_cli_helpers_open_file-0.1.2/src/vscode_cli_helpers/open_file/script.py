#! /usr/bin/env python3

import logging
import os
import platform
import subprocess
from pathlib import Path

import click

from vscode_cli_helpers.open_file.config import Config
from vscode_cli_helpers.open_file.exceptions import ConfigException


def add_extension(name: str) -> str:
    """Add the .py extension if it is missing."""
    if "." not in name:
        return name + ".py"
    else:
        return name


def edit_config_file(config: Config) -> None:
    """Edit the config file."""
    config_path = config.get_config_file()
    edit_file(config, config_path)


def edit_file(config: Config, file: Path) -> None:
    """Edit the config file."""
    cfg = config.config["Editor"]
    if platform.system() == "Linux":
        editor = cfg["Linux"]
        cmd = editor
        args = [str(file)]
    elif platform.system() == "Darwin":
        cmd = "open"
        editor = cfg["MacOS"]
        args = ["-a", editor, str(file)]
    elif platform.system() == "Windows":
        editor = cfg["Windows"]
        cmd = editor
        args = [str(file)]
    else:
        raise ConfigException(f"Unknown platform: {platform.system()}")
    logging.info(f"Running: {cmd} {args}")
    subprocess.Popen([cmd, *args], start_new_session=True)


def edit_template_file(config: Config) -> None:
    """Edit the template file."""
    path = config.get_template_dir("python")
    edit_file(config, path)


def find_code_workspace(dir_: Path) -> str:
    """Find the VSCode workspace for the given path."""
    workspaces = list(dir_.glob("*.code-workspace"))
    if len(workspaces) == 1:
        return Path(workspaces[0]).name
    else:
        return "."


@click.command()
@click.argument("path", type=str, default="t")
@click.option(
    "--edit-template", is_flag=True, default=False, help="Edit the template file"
)
@click.option("--edit-config", is_flag=True, default=False, help="Edit the config file")
def main(path: str, edit_template: bool, edit_config: bool) -> None:
    """``vscode-cli-helper-new-python-script`` is a command line tool for opening a new
    or existing Python script in VSCode and navigating to a specific line. Since this is
    a command you might use quite often, you may want to create a short alias for it like
    `ǹy``. See :doc:`Creating an alias <alias>` for more information.

    If the file does not exist, it will be created and made executable. Then a template
    will be written to the file before opening it in VS Code.

    EXAMPLES

    .. code-block:: bash

      $ vscode-cli-helper-new-python-script a.py

    Opens ``a.py`` in VS Code and navigates to line 1. If ``a.py`` does not exist, it will
    be created and made executable. Then a template will be written to the file before
    opening it in VS Code. ::

      $ vscode-cli-helper-new-python-script a

    If ``a`` exists, opens it in VS Code and navigates to line 1. If ``a`` does not exist,
    ``a.py`` will be created and made executable. Then a template will be written to the file
    before opening it in VSCode. ::

      $ vscode-cli-helper-new-python-script a:10
      $ vscode-cli-helper-new-python-script a.py:10

    Sames as above but also navigates to line 10

    For more information about editing the template file, see :doc:`Template <template>`.
    """
    logging.basicConfig(level=logging.INFO)
    config = Config()
    if edit_config:
        edit_config_file(config)
        return
    if edit_template:
        edit_template_file(config)
        return
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
