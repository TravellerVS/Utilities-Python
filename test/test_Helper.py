__author__ = 'Vedran Semenski <vedran.semenski@gmail.com>'

import unittest
from main.Helper import *

class HelperTestCase(unittest.TestCase):
    def test_string_is_not_empty(self):

        values_non_strings_or_empty = [None, True, False, "", '', 0, -1, 1, '''''', """"""]
        for value in values_non_strings_or_empty:
            self.assertEqual(HelperMethods.string_is_not_empty(value), False)

        values_strings = ['test', 'string', 'True', 'False', '0', '-1', '1', 'str',]
        for value in values_strings:
            self.assertEqual(HelperMethods.string_is_not_empty(value), True)

    def test_string_is_empty(self):

        values_non_strings_or_empty = [None, True, False, "", '', 0, -1, 1, '''''', """"""]
        for value in values_non_strings_or_empty:
            self.assertEqual(HelperMethods.string_is_empty(value), True)

        values_strings = ['test', 'string', 'True', 'False', '0', '-1', '1', 'str',]
        for value in values_strings:
            self.assertEqual(HelperMethods.string_is_empty(value), False)


if __name__ == '__main__':
    unittest.main()
