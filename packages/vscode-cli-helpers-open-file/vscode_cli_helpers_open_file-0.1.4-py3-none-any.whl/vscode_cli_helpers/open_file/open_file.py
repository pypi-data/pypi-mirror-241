import logging
import os
import platform
import shutil
import subprocess
from pathlib import Path
from typing import Optional

from vscode_cli_helpers.open_file.config import Config
from vscode_cli_helpers.open_file.exceptions import OpenFileException


class OpenFile:
    def __init__(self, path: Path, template_name: Optional[str]) -> None:
        self.path = path
        self.config = Config()
        if template_name is None:
            template_name = self.config.get_default_template_name()
        self.template_name = template_name
        filename = Path(path).name
        dir_ = Path(path).parent
        (basename, line_no) = (
            filename.split(":") if ":" in filename else (filename, None)
        )
        if basename is not None:
            filename = self.add_extension(basename)
        workspace = self.find_code_workspace(dir_)
        path2 = Path(dir_) / filename
        if not path2.exists():
            self.prepare_new_file(path2)
        else:
            logging.info(f"File exists: {path}")
        if line_no is not None:
            filename = f"{filename}:{line_no}"
        code = "code"
        if platform.system() == "Windows":  # pragma: no cover
            # See: https://stackoverflow.com/a/32799942/2173773
            tmp = shutil.which("code.cmd")
            if tmp is None:
                raise OpenFileException("Could not find code.cmd")
            code = tmp
        cmd = [code, "-g", filename, workspace]
        logging.info(f"Running: {cmd} in directory: {dir_}, workspace: {workspace}")
        subprocess.Popen(cmd, cwd=dir_, start_new_session=True)

    def add_extension(self, name: str) -> str:
        """Add the file extension if it is missing."""
        if "." not in name:
            ext = self.config.get_template_extension(self.template_name)
            logging.info(f"Adding extension: {ext} to file: {name}")
            return name + ext
        else:
            return name

    def find_code_workspace(self, dir_: Path) -> str:
        """Find the VSCode workspace for the given path."""
        workspaces = list(dir_.glob("*.code-workspace"))
        if len(workspaces) == 1:
            return Path(workspaces[0]).name
        else:
            return "."

    def prepare_new_file(self, path: Path) -> None:
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.config.get_template(self.template_name))
        logging.info(f"Creating file: {path}")
        if platform.system() == "Windows":
            logging.info("Not making file executable on Windows")
        else:
            if self.config.is_script(self.template_name):
                os.chmod(path, 0o755)
                logging.info(f"Setting file permissions to 755: {path}")
            else:
                logging.info(
                    f"Not script file type {self.template_name}. "
                    f"Not setting file permissions: {path}"
                )
