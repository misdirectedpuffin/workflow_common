"""Unit tests related to workflow_common.helper"""

import os
from configparser import ConfigParser
from unittest.mock import patch

from click.testing import CliRunner

import pytest
from workflow_common.helper import (aws_config_dir, get_config_file, get_profile,
                                    get_sections)


def test_get_profile_names(tmpdir):
    """It returns the expected config."""
    os.chdir(tmpdir)
    with open('config', 'w') as test_file:
        mock_config = ConfigParser()
        mock_config.add_section('Guido')
        mock_config.add_section('Raymond')
        mock_config.write(test_file)

    assert list(get_sections(tmpdir)) == ['Guido', 'Raymond']


@patch.dict('os.environ', {'HOME': '/user/home'})
def test_aws_config_dir():
    """It returns the expected directory."""
    assert aws_config_dir() == '/user/home/.aws'


def test_get_profile(tmpdir):
    """It returns the expected profile."""
    os.chdir(tmpdir)
    with open('config', 'w') as test_file:
        mock_config = ConfigParser()
        mock_config.add_section('profile')
        mock_config.set('profile', 'name', 'Guido')
        mock_config.write(test_file)
    assert get_profile(mock_config) == 'Guido'


@patch('workflow_common.helper.riser_config_dir')
def test_get_config_file(mock_config_dir):
    """It returns the expected path to config file."""
    mock_config_dir.return_value = '/foo/.bar'
    assert get_config_file() == '/foo/.bar/config'
