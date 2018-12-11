import time
import logging
from colorama import init, Fore, Style
from hexdump import dumpgen

# Init the colorama state
init()

class Logger(logging.Logger):
    """Generic Logger that prints both to stdout and an external log file

    Attributes:
        _name                       (str): name of the logger instance
        _timestamp                  (str): time stamp that is used for the log records
        _log_format                 (str): record log format using the following arguments: (timestamp, log type, log message)
        _min_level                 (enum): minimal logging level that should be recorded 
        _formatter       (LinesFormatter): basic formatter for FileHandler()s
        _color_formatter (ColorFormatter): colored formatter for the output handler (StreamHandler)

    Configurations:
        default_timestamp           (str): Default time stamp that is used for the log records
        default_log_format          (str): Default record log format: (timestamp, log type, log name, log message)
                                           NOTE: multiline comments assume that the message ends the record's line
        default_nameless_log_format (str): Default record log forma if has no namet: (timestamp, log type, log message)
    """

    default_timestamp           = "%d/%m/%Y %H:%M:%S"
    default_log_format          = "[%(asctime)s] - %(name)s - %(levelname)s: %(message)s"
    default_nameless_log_format = "[%(asctime)s] - %(levelname)s: %(message)s"

    def __init__(self, name, log_file_names = [], use_stdout = True, min_log_level = logging.INFO, timestamp = default_timestamp, log_format = default_log_format):
        """Configures the newly built logger instance

        Args:
            name                            (str): name for the logger instance
            log_files (tuple of tuples, optional): tuple of log files we should use: (log file name, open mode (, min log level))
            use_stdout        (boolean, optional): should we print to stdout? (True by default)
            min_log_level        (enum, optional): minimum log level. Value should be an enum option from the log level names (EVENT_LEVEL by default)
            timestamp             (str, optional): time format to be used in every log record (default_timestamp by default)
            log_format            (str, optional): overall format of the log records (default_log_format by default)
        """
        super(Logger, self).__init__(name)

        self._name       = name
        self._timestamp  = timestamp
        self._log_format = log_format
        self._min_level  = min_log_level

        if len(name) == 0 and self._log_format == Logger.default_log_format:
            self._log_format = Logger.default_nameless_log_format

        self.setLevel(logging.DEBUG)

        self._formatter = LinesFormatter(self._log_format, datefmt = self._timestamp)
        self._color_formatter = ColorFormatter(self._log_format, datefmt = self._timestamp)
        if use_stdout:
            out_handler = logging.StreamHandler()
            out_handler.setLevel(self._min_level)
            out_handler.setFormatter(self._color_formatter)
            self.addHandler(out_handler)

        for log_file_record in log_file_names:
            if len(log_file_record) == 2:
                file_name, open_mode = log_file_record
                file_min_level = min_log_level
            else:
                file_name, open_mode, file_min_level = log_file_record
            file_handler = logging.FileHandler(file_name, mode = open_mode)
            file_handler.setLevel(file_min_level)
            file_handler.setFormatter(self._formatter)
            self.addHandler(file_handler)

    def linkHandler(self, handler, log_level = None):
        """Links an additional custom handler

        Args:
            handler  (logging.Handler): custom handler
            log_level (enum, optional): minimal logging level (self._min_level by default)
        """

        if log_level is None :
            log_level = self._min_level
        handler.setLevel(log_level)
        handler.setFormatter(self._formatter)
        self.addHandler(handler)

    def setColor(self, log_level, style):
        """Updates the basic style for a specific logging level in the StreamHandler

        Args:
            log_level (enum): logging level (from logging)
            style    (style): colorama style for the desired logging level
        """
        self._color_formatter.setColor(log_level, style)

    def addIndent(self):
        """Adds an indentation level to the following log records shown on the stdout"""
        pass

    def removeIndent(self):
        """Removes an indentation level from the following log records shown on the stdout"""
        pass

    @staticmethod
    def _fixLines(record, prefix):
        """Updates a (possibly) multiline record, to better print the prefix

        Args:
            record (Logging.LogRecord): log record
            prefix               (str): string prefix to be added
        """
        raw_msg = record.msg
        if "\n" not in record.msg:
            record.msg = prefix + record.msg
        else:
            prefix_length = len(prefix)
            raw_msg = record.msg
            record.msg = ''
            for line in raw_msg.split("\n"):
                if len(record.msg) == 0:
                    record.msg += prefix + line + "\n"
                else:
                    record.msg += prefix_length * " " + line + "\n"
            # chop the last new line
            record.msg = record.msg[:-1]

class ColorFormatter(logging.Formatter):
    """Custom color formatter to be used by the std output handler of the Logger class

    Attributes:
        _log_styles (dict): a mapping between a log level's name and its style

    Configurations:
        default_colors (dict of type => color): <log level> => <colorama formatting>
    """

    default_colors  = {
                        logging.DEBUG:    Fore.LIGHTCYAN_EX, 
                        logging.INFO:     Fore.LIGHTWHITE_EX,
                        logging.WARN:     Fore.LIGHTYELLOW_EX,
                        logging.ERROR:    Fore.LIGHTRED_EX,
                        logging.CRITICAL: Fore.LIGHTRED_EX,
                      }

    def __init__(self, fmt=None, datefmt=None):
        """Default ctor"""
        super(ColorFormatter, self).__init__(fmt, datefmt)
        self._log_styles = dict(ColorFormatter.default_colors)

    def setColor(self, log_level, style):
        """Updates the basic style for a specific logging level

        Args:
            log_level (enum): logging level (from logging)
            style    (style): colorama style for the desired logging level
        """
        self._log_styles[log_level] = style

    def format(self, record):
        raw_msg = record.msg
        msg_args = record.args
        record.msg = ''
        record.args = []
        prefix = super(ColorFormatter, self).format(record)
        record.msg = raw_msg
        Logger._fixLines(record, prefix)
        record.args = msg_args
        result = self._log_styles[record.levelno] + super(ColorFormatter, self).format(record) + Style.RESET_ALL
        # restore the record
        record.msg = raw_msg
        # return the result
        return result

class LinesFormatter(logging.Formatter):
    """Custom formatter to add support for multiline records"""

    def __init__(self, fmt=None, datefmt=None):
        """Default ctor"""
        super(LinesFormatter, self).__init__(fmt, datefmt)

    def format(self, record):
        raw_msg = record.msg
        msg_args = record.args
        record.msg = ''
        record.args = []
        prefix = super(LinesFormatter, self).format(record)
        record.msg = raw_msg
        Logger._fixLines(record, prefix)
        record.args = msg_args
        result = super(LinesFormatter, self).format(record)
        # avoid a double prefix
        result = result[len(prefix):]
        # restore the record
        record.msg = raw_msg
        # return the result
        return result

def hexDump(data):
    """Prepares a hexdump string to be nicely printed by a logger

    Args:
        data (str): binary blob to be converted to a nice hexdump

    Return Value:
        absolute path to the created anchor directory
    """
    # Python StreamHandler uses '\n' as a terminator, so we are fine
    return '\n'.join(dumpgen(data))
