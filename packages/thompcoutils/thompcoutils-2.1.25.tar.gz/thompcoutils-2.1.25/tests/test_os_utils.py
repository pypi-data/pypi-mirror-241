import inspect
import os
import logging
import unittest
import run_me

from thompcoUtils.os_utils import script_is_running

test_path = 'test_ini_files'
if not os.path.exists(test_path):
    os.mkdir(test_path)
log_configuration_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.ini')
# noinspection PyUnresolvedReferences
logging.config.fileConfig(log_configuration_file)


class TestOsUtils(unittest.TestCase):
    def test_script_is_running(self):
        script_name = inspect.getfile(run_me)
        print(f'{script_name} is{" " if script_is_running(class_name=run_me) else " NOT "}running')

