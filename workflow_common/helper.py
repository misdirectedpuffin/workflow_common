# -*- coding: utf-8 -*-

"""Common module."""
import os
from configparser import ConfigParser

import click


def load(config_file: str):
    """Return the config object from the file path."""
    with open(config_file, 'r') as f:
        config = ConfigParser()
        config.read_file(f)
        return config


def get_sections(aws_dir):
    """Return a list of aws profile names."""
    config = ConfigParser()
    config.read(os.path.join(aws_dir, 'config'))
    for section in config.sections():
        yield section


def get_device_types(config_dir):
    """Return a list of device names"""
    config = ConfigParser()
    config.read(os.path.join(config_dir, 'config'))
    for section in config.sections():
        yield section


def aws_config_dir():
    """Return the absolute path to the aws config directory."""
    return os.path.join(
        '/',
        os.environ['HOME'],
        '.aws'
    )


def riser_config_dir():
    """Return the path to the config directory."""
    directory = click.get_app_dir('riser', force_posix=True)
    return directory


def get_profile(config):
    """Return the set profile name."""
    return config.get('profile', 'name')


def write(config: ConfigParser):
    """Write the config object to the config file."""
    with open(get_config_file(), 'w+') as f:
        config.write(f)
        return config


def get_config_file():
    """Return the abs path to the config file."""
    return os.path.join(riser_config_dir(), 'config')
