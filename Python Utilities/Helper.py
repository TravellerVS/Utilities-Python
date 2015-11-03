__author__ = 'Vedran Semenski <vedran.semenski@srce.hr>'



class HelperMethods(object):
    """
    HelperMethods contans a group of mostly static methods that are designed to contain often used parts of code and have them under one place.
    """

    @staticmethod
    def string_is_not_empty(s = None):
        """
        Method checks if the input string is equal to None, is and empty string of contains only whitespaces.
            if all of these are false the method returns false
        @type s: str
        @param s: input string for testing
        @rtype : bool False if the string is equal to None, is and empty string of contains only whitespaces, true otherwise.
        """
        result = False
        if isinstance(s, basestring) and (len(s) > 0) and (not s.isspace()):
            result = True
        return result

    @staticmethod
    def string_is_empty(s = None):
        """
        This method is the "not" version of the string_is_not_empty method.
        @type s: str
        @param s: input string for testing
        @rtype : bool - True if the string is equal to None, is and empty string of contains only whitespaces, false otherwise.
        """
        return (not HelperMethods.string_is_not_empty(s))
