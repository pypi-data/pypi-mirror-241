from argparse import Namespace
from pathlib import Path
import os
from dataclasses import dataclass
from unittest.mock import patch

from yaml import load
from yaml import Loader

from .app import CommandApp


class ConfigHandler:
    """
    Handle app-level configuration, where settings could come from specific
    settings (such as from argparse), environment variables, or a YAML file.
    """

    name = 'config'
    cache: dict = {}

    def __init__(self, value=None):
        self.file = value

    @property
    def yaml(self):
        if hasattr(self, '_yaml'):
            return self._yaml
        if self.file:
            path = Path(self.file)
        elif (envvar := self.env(self.appname + '-config')):
            path = Path(envvar)
        elif ((localpath := Path.cwd() / f".{self.appname}.yml").is_file()):
            path = localpath
        elif ((homepath := Path.home() / f".{self.appname}.yml").is_file()):
            path = homepath
        else:
            path = None
        if path:
            with open(path) as file:
                self._yaml = load(file, Loader=Loader)
                return self._yaml

    @staticmethod
    def env(name):
        if (envvar := name.upper().replace('-', '_')) in os.environ:
            return os.environ[envvar]

    def get(self, key: str):
        """Return the value for the requested config entry"""

        # If we already found the value, return it
        if key in self.cache:
            return self.cache[key]

        # Environment variables take precedence
        if (result := self.env(key)):
            self.cache[key] = result
            return result

        # Otherwise look at the YAML
        if (yaml := self.yaml):
            split = key.split('-')
            while (val := split.pop(0)) and (val in yaml):
                yaml = yaml[val] if val in yaml else None
                if not split:
                    self.cache[key] = yaml
                    return yaml

    # @classmethod
    # def add_app_args(self, parser):
    #     """Allows a Command class to also inherit from ConfigMachine. List
    #     ConfigMachine first."""
    #     parser.add_argument('--config', action='store')


def nohome_test():  # pragma: nocover
    """Fake out a ConfigMachine so that it thinks test/files is the home
    directory. This way it's not tempted to pull real configuration."""
    return patch('pathlib.Path.home', lambda: Path('test/files'))


def patchconfig_test(**kwargs):  # pragma: nocover
    """Hand testable config data to a test method."""
    methodpath = 'wizlib.config_machine.ConfigMachine.get'

    def configpatch(self, key):
        key = key.replace('-', '_')
        return kwargs[key] if (key in kwargs) else None
    return patch(methodpath, configpatch)
