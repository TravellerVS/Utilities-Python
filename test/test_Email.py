from smtplib import SMTPServerDisconnected

__author__ = 'Vedran Semenski <vedran.semenski@gmail.com>'

import unittest
from config import *

class EmailTestCase(unittest.TestCase):

    def setUp(self):
        self.__EmailHandler = initialize_email() #EmailHandler(config={'type': 'SMTP','host':'smtp.srce.hr','port':25})
    def tearDown(self):
        pass

    def test_init(self):
        # just check it runs without exceptions
        self.assertIsInstance(self.__EmailHandler, EmailHandler, "Initialisation was not successful")

    def test_send_email(self):
        # just check it runs without exceptions
        self.__EmailHandler.send_email(subject='Test',sender='test@test.com', recipients=['test@test.com'],message='Test Message')


if __name__ == '__main__':
    initialize_email()
    unittest.main()
