'''
Created on 28. ruj 2015.

@author: "Vedran Semenski"
'''

import mysql.connector
from mysql.connector import errorcode

import datetime
# from mysql.connector.cursor import MySQLCursorPrepared

from com.srce.RADIUS.utils.Helper import HelperMethods
import Singleton

class DatabaseException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class DatabaseHandler(object):
    """
    The DatabaseHandler contains database related functionality.
    """

    # Transforms this class into a Singleton
    __metaclass__ = Singleton.Singleton

    def __init__(self, config = None):
        """
        @type config: dict
        @rtype : DatabaseHandler
        """
        self.__cnx = None
        self.__config = config
        self.__connect()

    def __connect(self):

        if self.__config is None:
            self.__config = {
                      'user': '',
                      'password': '',
                      'host': 'localhost',
                      'database': 'test',
                      'raise_on_warnings': True,
                      'use_pure': False,
            }

        try:
            self.__cnx = mysql.connector.connect(**self.__config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("Unknown error: " + err)
            self.__del__()
            raise
        # else:
        #     print("Connection successfull")

    @property
    def connection(self):
        """

        :rtype : object - mysql.connector
        """
        return self.__cnx

    def __del__ (self):
        if self.__cnx is not None:
            self.__cnx.close()
        else:
            pass    #do nothing and continue deletion


    def execute_query(self, query = ""):
        """
        The function executes the given query and returns the cursor.

        :param query: The query that will be executed
        :type query: str
        :rtype :object - mysql.connector.cursor
        """
        cursor = None
        if HelperMethods.string_is_not_empty(query):
            cursor = self.connection.cursor()
            try:
                cursor.execute(query)
            except (DatabaseException, Exception) as e:
                # open space for possible error handling
                raise
        return cursor
