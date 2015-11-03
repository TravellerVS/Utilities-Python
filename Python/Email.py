from Helper import HelperMethods

__author__ = 'Vedran Semenski<vedran.semenski@gmail.com>'


# Import smtplib for the actual sending function
import smtplib
from email.mime.text import MIMEText



class EmailHandler(object):
    """
    The EmailHandler contains email related functionality.
    """
    def __init__(self, server = None,
                 config = {
                        'type': 'SMTP',
                        'host': 'localhost',
                        'port': None,
                        'username': None,
                        'password': None
                }):
        """

        :rtype : EmailHandler
        @type server: smtplib.SMTP
        """
        self.__config = config
        self.__server = server

    def __set_default_server(self):
        server = None
        if(self.__config.get('type').lower() == 'smtp'):
            if any(self.__config.get('host').lower() in s for s in ['localhost', '127.0.0.1']):
                server = smtplib.SMTP(self.__config.get('host'))
            elif ( HelperMethods.string_is_not_empty(self.__config.get('host')) and HelperMethods.string_is_not_empty(self.__config.get('host')) ):
                # server = smtplib.SMTP(self.__config.get('host'),self.__config.get('port'))
                if ( HelperMethods.string_is_not_empty(self.__config.get('username')) and HelperMethods.string_is_not_empty(self.__config.get('password')) ):
                    # TODO make username/password/login type email sending work
                    raise NotImplementedError("Configuration with username and password isn\'t yet implemented and tested ")

                    server = smtplib.SMTP(self.__config.get('host'),self.__config.get('port'))
                    server.starttls()
                    # server.connect(self.__config.get('host'),self.__config.get('port'))
                    server.login(self.__config.get('username'), self.__config.get('password'))
                else:
                    server = smtplib.SMTP()
                    server.connect(self.__config.get('host'),self.__config.get('port'))
            else:
                raise NotImplementedError("This Email Configuration isn\'t supported.")
                pass

        self.__server=server

    @property
    def __server(self):
        if self.__server_val is None:
            self.__set_default_server()
        return self.__server_val

    @__server.setter
    def __server(self, server):
        """
        @type server: smtplib.SMTP
        """
        if server is None:
            self.__set_default_server()
        else:
            self.__server_val = server

    def send_email(self, subject=None, sender=None, recipients=None, message=None):
        """
        @type subject: str
        @type sender: str
        @type recipients: list
        @type message: str
        @param subject: The Subject in the email
        @param sender: The sender's email address
        @param recipients: List of email addresses of the recipients
        @param message: The body of the email
        """
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ", ".join(recipients)
        self.__server.sendmail(sender, recipients, msg.as_string())

    def __del__(self):
        if self.__server_val is not None:
            self.__server.quit()
