#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import UserDict
from configparser import ConfigParser
import os
import platform


if os.name == 'posix':

    DEFAULTS = dict(
        download_path=os.path.expanduser("~/Youtube/"),
        db_file_path=os.path.expanduser("~/.config/aldemsubs/database.sqlite"),
        mark_videos_old_after=5,  # days
        delete_downloads_after=5,  # days
        after_subscribe_download_n_videos=3,
    )

elif platform.system() == 'Windows':

    DEFAULTS = dict(
        download_path=os.path.expandvars("%USERPROFILE%\\Youtube\\"),
        db_file_path=os.path.expandvars("%APPDATA%\\aldemsubs\\database.sqlite"),
        mark_videos_old_after=5,  # days
        delete_downloads_after=5,  # days
        after_subscribe_download_n_videos=3,
    )


class ConfigHandler(UserDict):

    def __init__(self, config_file_path=""):
        super().__init__(**DEFAULTS)
        config_file_path = os.path.expanduser(config_file_path)
        if os.path.isfile(config_file_path):
            self.load_config(config_file_path)

    def load_config(self, config_file_path):
        config = ConfigParser()
        config.read(config_file_path)

        if not self.all_settings_valid(config):
            raise ConfigError("Invalid keys found.")

        self.data.update(config['aldemsubs'])

        # fix values and types

        # Windows compatibility
        if os.name == 'posix':
            self.data["download_path"] = os.path.expanduser(
                self.data["download_path"])
            self.data["db_file_path"] = os.path.expanduser(
                self.data["db_file_path"])
        elif platform.system() == 'Windows':
            self.data["download_path"] = os.path.expandvars(
                self.data["download_path"])
            self.data["db_file_path"] = os.path.expandvars(
                self.data["db_file_path"])

        self.data["mark_videos_old_after"] = int(
            self.data["mark_videos_old_after"])
        self.data["delete_downloads_after"] = int(
            self.data["delete_downloads_after"])
        self.data["after_subscribe_download_n_videos"] = int(
            self.data["after_subscribe_download_n_videos"])

    def all_settings_valid(self, config):
        return set(config['aldemsubs'].keys()).issubset(self.data.keys())


class ConfigError(Exception):
    pass
