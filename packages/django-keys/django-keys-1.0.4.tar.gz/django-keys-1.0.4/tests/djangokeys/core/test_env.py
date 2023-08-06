#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for reading environment variables from .env file.

from djangokeys.core.env import read_values_from_env

from tests.files import EXAMPLE1_ENV_PATH
from tests.utils.environment_vars import use_environment_variable


def test__read_values_from_env__file_does_not_exist():
    """ Tests that an empty directory is returned when .env doesn't exist.
    """
    values = read_values_from_env("does_not_exist.env")
    assert type(values) == dict
    assert len(values) == 0


def test__read_values_from_env__file_exists():
    """ Tests that values are successfully read from file.
    """
    values = read_values_from_env(EXAMPLE1_ENV_PATH)
    assert values["DOMAIN"] == "example.org"
    assert values["ADMIN_EMAIL"] == "admin@example.org"
    assert values["ROOT_URL"] == "example.org/app"
    assert values["HELLO"] == "nobody answers back"


def test__read_values_from_env__cant_read_execution_environment():
    """ Environment variables set by execution environment aren't accessed.
    """
    with use_environment_variable('EV_123', 'value'):
        values = read_values_from_env(EXAMPLE1_ENV_PATH)
        assert 'EV_123' not in values
