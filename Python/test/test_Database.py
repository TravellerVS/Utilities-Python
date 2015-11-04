
__author__ = 'Vedran Semenski <vedran.semenski@gmail.com>'

import unittest

from config import *

class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.__DBHandler = initialize_database()#DatabaseHandler()

    def tearDown(self):
        pass

    def test_init(self):
        self.assertIsInstance(self.__DBHandler, DatabaseHandler, "Initialisation was not successful")

    def test_connection(self):
        self.assertIsNotNone (self.__DBHandler.connection, "Connection to database failed")

if __name__ == '__main__':
    unittest.main()
