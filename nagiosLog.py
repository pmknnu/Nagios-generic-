
__author__ = 'SRIDHAR GUDE'


import logging
from logging.handlers import RotatingFileHandler


_logger_name = "Nagios"
_print_format = "%(asctime)s - %(levelname)s - %(message)s"
_level = logging.DEBUG

class nagiosLog():
    """
    It takes "log_file" as mandatory argument and logs the messages to provided
    log file. It doesn't output anything on the console.

    You have to use required print statements to post the output to console and
    Nagios Dashboard,this is due to limitation we have for Nagios since printing
    everything we log on to file to Nagios dashboard will be clumsy.

    On Nagios dashboard, it's preferred to have a one line statement explaining
    the state.

    """

    def __init__(self,log_file,logger_name=_logger_name,level=_level):

        self.log_file = log_file
        self.logger_name = logger_name
        self.level = level

    def getLog(self):

        """
        Return the logging object

        """
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(self.level)
        logger.addHandler(self._rotateLog())

        return logger

    def _rotateLog(self):

        """
        Rotating the log files if it exceed the size.
        The default size is 20 MB with 2 backupfiles
        """

        rh = RotatingFileHandler(self.log_file,
                                 maxBytes=20*1024*1024, backupCount=2)
        formatter = logging.Formatter(_print_format)
        rh.setFormatter(formatter)
        return rh

