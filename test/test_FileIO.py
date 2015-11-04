__author__ = 'Vedran Semenski <vedran.semenski@gmail.com>'

import unittest

from config import *
from main.FileIO import FileIOHandler

class FileIOTestCase(unittest.TestCase):

    def test_check_rejects(self):
        filepath = os.path.dirname(os.path.realpath(__file__))+os.sep+CONFIG_FILENAME
        content = FileIOHandler.read_all(filepath)
        self.assertIsNotNone(content, "FileIO retrieved object that is None.")
        self.assertIsInstance(content,str,"FileIO retrieved object that is not str.")

        
if __name__ == '__main__':
    unittest.main()
