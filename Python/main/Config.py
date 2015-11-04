__author__ = 'Vedran Semenski <vedran.semenski@gmail.com>'

import ConfigParser
import ast

import Singleton


class ConfigHandler(object):
    """
    __metaclass__ = Singleton.Singleton is used for making the ConfigHandler a Singleton
    @see Singleton.Singleton
    """
    __metaclass__ = Singleton.Singleton

    __DEFAULT_CONFIG_FILENAME = 'project.config'

    def __init__(self, configFile = __DEFAULT_CONFIG_FILENAME):
        """
        @param configFile: name/location of the configuration filename
                default value __DEFAULT_CONFIG_FILENAME is 'project.config'
        @type configFile: str
        """

        self.set_new_config_file(configFile=configFile)

    @property
    def config(self):
        """
        @rtype : ConfigParser.RawConfigParser
        @return: raturns the RawConfigParser object of initially created ConfigHandler
        """
        return self.__config

    @config.setter
    def config(self,config = None):
        pass

    def set_new_config_file(self, configFile = __DEFAULT_CONFIG_FILENAME):
        """
        @param configFile: name/location of the configuration filename
                default value __DEFAULT_CONFIG_FILENAME is 'project.config'
        @type configFile: str
        """
        self.__config = ConfigParser.RawConfigParser()
        self.__config.read(configFile)

    def get_parsed_value(self,section, option):
        """
        Returns a parsed value of the input string from the .config file.
        The parsing is done by ast.literal_eval(input_string)
        @rtype : dict
        @param section:
        @type section: str
        @param option:
        @type option: str
        @return: returns dictionary of the selected string section and option
        """
        return ast.literal_eval(self.config.get(section, option))

    def __del__(self):
        self.__config = None
