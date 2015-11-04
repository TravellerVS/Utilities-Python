__author__ = 'Vedran Semenski <vedran.semenski@gmail.com>'

from main.Config import ConfigHandler
from main.Database import DatabaseHandler
from main.Helper import HelperMethods
from main.Email import EmailHandler

import os
import logging

# This .config file needs to be set for the configuration to work
CONFIG_FILENAME = 'test.config'
SQL_DIR_FULLPATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__ )))+ os.sep + "sql" + os.sep # assign the directory name to this global variable and add the a separator at the end
RESPONSE_LOG_TABLE_NAME = 'proxy_response_log'

def initialize_config(filepath = None):
    """
    Initializes and returns the ConfigHandler.
    The configuration for the Configuration Handler is taken from CONFIG_FILENAME = 'test.config'
    @type filepath: str
    @param filepath: Full file path of config file.
                        If this parameter is None or and empty string the default project.config file is used
    @rtype : main.Config.ConfigHandler
    """
    ch = None
    if (HelperMethods.string_is_empty(filepath)):
        filepath = os.path.dirname(os.path.realpath(__file__))+os.sep+CONFIG_FILENAME
    ch = ConfigHandler(filepath)
    return ch

def initialize_database(config_filepath = None):
    """
    Initializes and returns the DatabaseHandler
    The configuration for the Database Handler is taken from the config file
    @rtype : main.Database.DatabaseHandler
    @type config_filepath: str
    @param config_filepath: Full file path of config file.
                            If this parameter is None or and empty string the default project.config file is used
    """

    ch = initialize_config(config_filepath)
    mysql_config = ch.get_parsed_value('Database','mysql_config')
    dbHandler = DatabaseHandler(mysql_config)
    return dbHandler

def initialize_email(config_filepath = None):
    """
    Initializes and returns the EmailHandler
    The configuration for the Email Handler is taken from the config file
    @rtype : main.Email.EmailHandler
    @type config_filepath: str
    @param config_filepath: Full file path of config file.
                            If this parameter is None or and empty string the default project.config file is used
    """
    ch = initialize_config(config_filepath)
    email_config = ch.get_parsed_value('Email', 'smtp_config')
    emailHandler = EmailHandler(config = email_config)
    return emailHandler

def initialize_log(config_filepath = None):
    """
    Initializes and configures the logging entity
    @rtype : logging
    @type config_filepath: str
    @param config_filepath: Full file path of config file.
                            If this parameter is None or and empty string the default project.config file is used
    """
    ch = initialize_config(config_filepath)
    log_file_name = ch.get_parsed_value('Log', 'log_file_name')
    logging.basicConfig(format='%(asctime)s-%(levelname)s:%(message)s', level=logging.DEBUG, filename=log_file_name)

def initialize_all(config_filepath = None):
    """
    Initializes all "Handler" type entities and the logging entity (from logging).
    These include the: ConfigHandler, DatabaseHandler, EmailHandler and logging
    @type config_filepath: str
    @param config_filepath: Full file path of config file.
                            If this parameter is None or and empty string the default project.config file is used
    """
    initialize_config(config_filepath)
    initialize_log()
    initialize_database()
    initialize_email()

if __name__ == '__main__':
    initialize_all()