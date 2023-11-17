import configparser
import importlib.resources
import logging
from configparser import ConfigParser
from pathlib import Path

import platformdirs

from vscode_cli_helpers.open_file.exceptions import ConfigException


class Config:
    # NOTE: These are made class variables since they must be accessible from
    #   pytest before creating an object of this class
    dirlock_fn = ".dirlock"
    config_fn = "config.ini"
    appname = "vscode-cli-helper-open-script"

    def __init__(self) -> None:
        self.lockfile_string = "author=HH"
        self.config_dir = self.get_config_dir()
        self.config_path = Path(self.config_dir) / self.config_fn
        self.read_config()

    def check_correct_config_dir(self, lock_file: Path) -> None:
        """The config dir might be owned by another app with the same name"""
        if lock_file.exists():
            if lock_file.is_file():
                with open(str(lock_file), encoding="utf_8") as fp:
                    line = fp.readline()
                    if line.startswith(self.lockfile_string):
                        return
                msg = "bad content"
            else:
                msg = "is a directory"
        else:
            msg = "missing"
        raise ConfigException(
            f"Unexpected: Config dir lock file: {msg}. "
            f"The data directory {str(lock_file.parent)} might be owned by another app."
        )

    def get_config_dir(self) -> Path:
        config_dir = platformdirs.user_config_dir(appname=self.appname)
        path = Path(config_dir)
        lock_file = path / self.dirlock_fn
        if path.exists():
            if path.is_file():
                raise ConfigException(
                    f"Config directory {str(path)} is file. Expected directory"
                )
            self.check_correct_config_dir(lock_file)
        else:
            path.mkdir(parents=True)
            with open(str(lock_file), "a", encoding="utf_8") as fp:
                fp.write(self.lockfile_string)
        return path

    def get_config_file(self) -> Path:
        return self.config_path

    def get_template(self, language: str) -> str:
        path = self.get_template_dir(language)
        logging.info(f"Reading {language} template from: {path}")
        with open(str(path), "r", encoding="utf_8") as fp:
            return fp.read()

    def get_template_dir(self, language: str) -> Path:
        dir_ = self.get_config_dir()
        template_dir = dir_ / "templates"
        if not template_dir.exists():
            template_dir.mkdir(parents=True)
        path = template_dir / f"{language}.txt"
        if not path.exists():
            def_path = importlib.resources.files(
                "vscode_cli_helpers.open_file.data.templates"
            ).joinpath(f"{language}.txt")
            with open(str(def_path), "r", encoding="utf_8") as fp:
                template = fp.read()
            with open(path, "w", encoding="utf_8") as fp:
                fp.write(template)
        return path

    def read_config(self) -> None:
        path = self.get_config_file()
        if path.exists():
            if not path.is_file():
                raise ConfigException(
                    f"Config filename {str(path)} exists, but filetype is not file"
                )
        else:
            with open(path, "w", encoding="utf_8") as _:
                pass  # only create empty file
        config = configparser.ConfigParser()
        self.read_defaults(config)
        config.read(str(path))
        logging.info(f"Read config file: {str(path)}")
        self.config = config

    def read_defaults(self, config: ConfigParser) -> None:
        path = importlib.resources.files("vscode_cli_helpers.open_file.data").joinpath(
            "default_config.ini"
        )
        config.read(str(path))
