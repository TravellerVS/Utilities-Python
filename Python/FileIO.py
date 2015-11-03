__author__ = 'Vedran Semenski <vedran.semenski@gmail.com>'



class FileIOHandler(object):
    """
    FileIOHandler encapsulates the standard IO functions for easier use by other parts of the code and reduce lines of code.
    """

    @staticmethod
    def read_all(full_filepath = ""):
        """
        This method is the "not" version of the string_is_not_empty method.
        @type full_filepath: str
        @param full_filepath: input string for testing
        @rtype : str - returns the full contents of a file in a string format
        """
        f = open(full_filepath,'r')
        file_content = f.read()      # Using .readlines()
        f.close()
        return file_content