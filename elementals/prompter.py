import logging
from logger import Logger, ColorFormatter
from colorama import Style

class Prompter(Logger):
    """Exploit oriented cmd prompter, uses logger behind the scenes

    Attributes:
        _prompter_formatter (PrompterFormatter): prompter formatter for the output handler (StreamHandler)
    """

    def __init__(self, name = '', log_file_names = [], min_log_level = logging.INFO, timestamp = Logger.default_timestamp, log_format = Logger.default_log_format):
        """Configures the newly built prompter instance

        Args:
            name                  (str, optional): name of the logger instance (no name by default)
            log_files (tuple of tuples, optional): tuple of log files we should use: (log file name, open mode (, min log level))
            min_log_level        (enum, optional): minimum log level. Value should be an enum option from the log level names (EVENT_LEVEL by default)
            timestamp             (str, optional): time format to be used in every log record (default_timestamp by default)
            log_format            (str, optional): overall format of the log records (default_log_format by default)
        """
        super(Prompter, self).__init__(name, log_file_names, use_stdout = False, min_log_level = min_log_level, timestamp = timestamp, log_format = log_format)
        self._prompter_formatter = PrompterFormatter()
        out_handler = logging.StreamHandler()
        out_handler.setLevel(self._min_level)
        out_handler.setFormatter(self._prompter_formatter)
        self.addHandler(out_handler)

    def setPrefix(self, log_level, prefix):
        """Updates the basic style for a specific logging level

        Args:
            log_level (enum): logging level (from logging)
            prefix   (style): string prefix for the desired logging level
        """
        self._prompter_formatter.setPrefix(log_level, prefix)

    def setColor(self, log_level, style):
        """Updates the basic style for a specific logging level in the StreamHandler

        Args:
            log_level (enum): logging level (from logging)
            style    (style): colorama style for the desired logging level
        """
        self._prompter_formatter.setColor(log_level, style)

    def addIndent(self):
        self._prompter_formatter.addIndent()

    def removeIndent(self):
        self._prompter_formatter.removeIndent()

class PrompterFormatter(ColorFormatter):
    """Custom metasploit-style formatter to be used by the std output handler of the Prompter class

    Attributes:
        _level_masking (dict): a mapping between a log level's name and its string prefix
        _indents        (int): indentation level 

    Configurations:
        default_level_masking (dict of type => str): <log level> => <prefix string>
    """

    default_level_masking = { 
                             logging.DEBUG:    '[$]', 
                             logging.INFO:     '[+]',
                             logging.WARN:     '[*]',
                             logging.ERROR:    '[!]',
                             logging.CRITICAL: '[!]',
                            }

    def __init__(self, fmt=None, datefmt=None):
        """Default ctor"""
        super(PrompterFormatter, self).__init__(fmt, datefmt)

        self._level_masking = dict(PrompterFormatter.default_level_masking)
        self._indents       = 0

    def setPrefix(self, log_level, prefix):
        """Updates the basic style for a specific logging level

        Args:
            log_level (enum): logging level (from logging)
            prefix   (style): string prefix for the desired logging level
        """
        self._level_masking[log_level] = prefix

    def addIndent(self):
        self._indents += 1

    def removeIndent(self):
        if self._indents <= 0:
            raise Exception("Indentation can not be decreased to negative values")
        self._indents -= 1

    def format(self, record):
        record.msg = self._indents * 4 * " " + self._level_masking[record.levelno] + " " + record.msg
        return super(PrompterFormatter, self).format(record)
