__author__ = 'Vedran Semenski <vedran.semenski@gmail.com>'

import unittest
import ConfigParser
from config import *
from main.Config import ConfigHandler

class ConfigTestCase(unittest.TestCase):

    def setUp(self):
        # initialize_all()
        self.__ConfigHandler = initialize_config()

    def tearDown(self):
        pass

    def test_init(self):
        self.assertIsInstance(self.__ConfigHandler, ConfigHandler, "Initialisation was not successful")

    def test_check_config(self):
        config = self.__ConfigHandler.config
        self.assertIsInstance(config, ConfigParser.RawConfigParser, "ConfigParser.config is of the wrong type")

    def test_check_config_values(self):
        config = self.__ConfigHandler.config
        self.assertIsInstance(config.sections(), list, "Sections are of the wrong type")
        self.assertIsInstance(config.getboolean('Section1', 'optionBoolean'), bool, "Boolean option is of the wrong type")
        self.assertIsInstance(config.get('Section1', 'optionString'), str, "String option is of the wrong type")
        self.assertIsInstance(config.getint('Section1', 'optionInteger'), int, "Integer option is of the wrong type")

        self.assertIsInstance(config.getboolean('Section2', 'optionBoolean'), bool, "Boolean option is of the wrong type")
        self.assertIsInstance(config.get('Section2', 'optionString'), str, "String option is of the wrong type")
        self.assertIsInstance(config.getint('Section2', 'optionInteger'), int, "Integer option is of the wrong type")

    def test_singleton(self):
        conf1 = initialize_config()
        conf2 = ConfigHandler()
        self.assertIs(self.__ConfigHandler,conf1, "Singleton Problem, different calls do not result in the same instance")
        self.assertIs(self.__ConfigHandler,conf2, "Singleton Problem, different calls do not result in the same instance")

    def test_logging(self):
        initialize_log('test.log')
        logging.info("running_test")
        logging.debug("running_test")
        logging.critical("running_test")

if __name__ == '__main__':
    initialize_config()
    unittest.main()
