import os
import logging
import unittest

from thompcoUtils.os_utils import script_is_running

test_path = 'test_ini_files'
if not os.path.exists(test_path):
    os.mkdir(test_path)
log_configuration_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.ini')
# noinspection PyUnresolvedReferences
logging.config.fileConfig(log_configuration_file)


class TestOsUtils(unittest.TestCase):
    def test_script_is_running(self):
        script_name = 'script_name.py'
        script_is_running(script_name=script_name)
