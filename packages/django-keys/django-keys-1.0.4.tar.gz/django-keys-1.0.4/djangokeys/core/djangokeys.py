#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains DjangoKeys class.

from os import getenv

import djangokeys.utils.logging as logger

from djangokeys.core.env import read_values_from_env
from djangokeys.exceptions import EnvironmentVariableNotFound
from djangokeys.exceptions import ValueTypeMismatch
from djangokeys.exceptions import ValueIsEmpty


class DjangoKeys:
    """ Used to access values of environment variables that have been set by
        the execution environment, or are listed in an .env file.

        - environment variables specified by the .env file cannot overwrite
          environment variables set by the execution environment, unless
          `overwrite=True` when accessing the environment variable
        - the usage of a .env file is optional, so if no .env file exists at
          the specified location, the program continues silently
    """

    def __init__(self, path=".env"):
        """ Initializes a new instance of DjangoKeys.

        The usage of a .env file is optional. Therefore, if no .env file exists
        at the specified location, the program continues silently.

        :param str path: filepath to .env file containing environment vars
        """
        self._path = path
        self._values = read_values_from_env(path)

    def secret_key(self, key, *, overwrite=False):
        """ Access environment variable used to store value of Django's
            SECRET_KEY setting.

        :param str key: name of environment variable
        :param bool overwrite: .env file can overwrite execution environment

        :rtype: str
        :returns: value of environment variable as a string

        :raises EnvironmentVariableNotFound: environment variable not set
        """
        value = self._get_value(key, overwrite=overwrite)
        if value == "":
            msg = "Environment variable '{}' cannot be empty; is secret key."
            raise ValueIsEmpty(msg.format(key))
        return value

    def str(self, key, *, overwrite=False):
        """ Access environment variable as a simple string.

        :param str key: name of environment variable
        :param bool overwrite: .env file can overwrite execution environment

        :rtype: str
        :returns: value of environment variable as a string

        :raises EnvironmentVariableNotFound: environment variable not set
        """
        return self._get_value(key, overwrite=overwrite)

    def int(self, key, *, overwrite=False):
        """ Access environment variable as an integer.

        :param str key: name of environment variable
        :param bool overwrite: .env file can overwrite execution environment

        :rtype: int
        :returns: value of environment variable as an integer

        :raises EnvironmentVariableNotFound: environment variable not set
        :raises ValueTypeMismatch: value cannot be interpreted as an int
        """
        value = self._get_value(key, overwrite)
        if value == "":
            msg = "Environment variable '{}' is empty; expected int."
            raise ValueIsEmpty(msg.format(key))
        try:
            value = int(value)
        except ValueError:
            msg = "Could not interpret environment variable '{}' as int: {}"
            raise ValueTypeMismatch(msg.format(key, value))
        return value

    def float(self, key, *, overwrite=False):
        """ Access environment variable as an integer.

        :param str key: name of environment variable
        :param bool overwrite: .env file can overwrite execution environment

        :rtype: int
        :returns: value of environment variable as an integer

        :raises EnvironmentVariableNotFound: environment variable not set
        :raises ValueTypeMismatch: value cannot be interpreted as an int
        """
        value = self._get_value(key, overwrite)
        if value == "":
            msg = "Environment variable '{}' is empty; expected float."
            raise ValueIsEmpty(msg.format(key))
        try:
            value = float(value)
        except ValueError:
            msg = "Could not interpret environment variable '{}' as float: {}"
            raise ValueTypeMismatch(msg.format(key, value))
        return value

    def bool(self, key, *, overwrite=False):
        """ Access environment variable as a boolean.

        :param str key: name of environment variable
        :param bool overwrite: .env file can overwrite execution environment

        :rtype: bool
        :returns: value of environment variable as an bool

        :raises EnvironmentVariableNotFound: environment variable not set
        :raises ValueTypeMismatch: value cannot be interpreted as a bool
        """
        value = self._get_value(key, overwrite).lower().strip()
        if value == "":
            msg = "Value of environment variable '{}' is empty, expects bool."
            raise ValueIsEmpty(msg.format(key))
        if value in ["f", "false", "0", "n", "no"]:
            return False
        if value in ["t", "true", "1", "y", "yes"]:
            return True
        msg = "Could not interpret environment variable '{}' as bool: {}"
        raise ValueTypeMismatch(msg.format(key, value))

    def _get_value(self, key, overwrite):
        """ Used internally to retrieve value of environment variable.
        """
        value_set_by_env = getenv(key)
        value_set_by_file = self._values.get(key, None)
        if value_set_by_env is None and value_set_by_file is None:
            msg = "Could not find an environment variable '{}'"
            raise EnvironmentVariableNotFound(msg.format(key))
        elif value_set_by_env is None and value_set_by_file is not None:
            msg = "Using environment variable '{}' set by environment."
            logger.info(msg.format(key))
            return value_set_by_file
        elif value_set_by_env is not None and value_set_by_file is None:
            msg = "Using environment variable '{}' set by environment."
            logger.info(msg.format(key))
            return value_set_by_env
        elif overwrite:
            msg = "Overwriting environment variable '{}':" \
                  "using environment variable set by .env file."
            logger.warning(msg.format(key))
            return value_set_by_file
        else:
            msg = "Overwriting environment variable '{}' not allowed:" \
                  "using environment variable set by environment."
            logger.warning(msg.format(key))
            return value_set_by_env

    def report_problems(self):
        """ Reports any problems after having been used, such as unused
            environment variables specified in .env file.
        """
        # TODO: implement warnings for problems
        logger.warning("nothing wrong detected...")
