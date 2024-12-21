import logging
from .logger        import Logger, ColorFormatter
from six.moves      import input

class Prompter(Logger):
    """Exploit oriented cmd prompter, uses logger behind the scenes.

    Attributes
    ----------
        _prompter_formatter (PrompterFormatter): prompter formatter for the output handler (StreamHandler)
    """

    def __init__(self, name='', log_file_names=[], min_log_level=logging.INFO, timestamp=Logger.default_timestamp, log_format=Logger.default_log_format):
        """Configure the newly built prompter instance.

        Args:
            name                  (str, optional): name of the logger instance (no name by default)
            log_files (tuple of tuples, optional): tuple of log files we should use: (log file name, open mode (, min log level))
            min_log_level        (enum, optional): minimum log level. Value should be an enum option from the log level names (logging.INFO by default)
            timestamp             (str, optional): time format to be used in every log record (default_timestamp by default)
            log_format            (str, optional): overall format of the log records (default_log_format by default)
        """
        super(Prompter, self).__init__(name, log_file_names, use_stdout=False, min_log_level=min_log_level, timestamp=timestamp, log_format=log_format)
        self._prompter_formatter = PrompterFormatter()
        out_handler = logging.StreamHandler()
        out_handler.setLevel(self._min_level)
        out_handler.setFormatter(self._prompter_formatter)
        self.addHandler(out_handler)

    def setPrefix(self, log_level, prefix):
        """Update the basic style for a specific logging level.

        Args:
            log_level (enum): logging level (from logging)
            prefix   (style): string prefix for the desired logging level
        """
        self._prompter_formatter.setPrefix(log_level, prefix)

    def setColor(self, log_level, style):
        """Update the basic style for a specific logging level in the StreamHandler.

        Args:
            log_level (enum): logging level (from logging)
            style    (style): colorama style for the desired logging level
        """
        self._prompter_formatter.setColor(log_level, style)

    def addIndent(self):
        """Add an indentation level to the following log records shown on the stdout."""
        self._prompter_formatter.addIndent()

    def removeIndent(self):
        """Remove an indentation level from the following log records shown on the stdout."""
        self._prompter_formatter.removeIndent()

    def input(self, msg):
        """Prompt the user for a given input, using the same meta-sploit styled prefix.

        Args:
            msg (str): message that would be shown to the user when asking for his input

        Return Value:
            User input string, as returned by "raw_input"
        """
        return input(self._prompter_formatter.calcPrefix() + msg)

class PrompterFormatter(ColorFormatter):
    """Custom metasploit-style formatter to be used by the std output handler of the Prompter class.

    Attributes
    ----------
        _level_masking (dict): a mapping between a log level's name and its string prefix
        _indents        (int): indentation level

    Configurations
    --------------
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
        """Create the base instance."""
        super(PrompterFormatter, self).__init__(fmt, datefmt)

        self._level_masking = dict(PrompterFormatter.default_level_masking)
        self._indents       = 0

    def setPrefix(self, log_level, prefix):
        """Update the basic style for a specific logging level.

        Args:
            log_level (enum): logging level (from logging)
            prefix   (style): string prefix for the desired logging level
        """
        self._level_masking[log_level] = prefix

    def addIndent(self):
        """Add an indentation level to the following log records shown on the stdout."""
        self._indents += 1

    def removeIndent(self):
        """Remove an indentation level from the following log records shown on the stdout."""
        if self._indents <= 0:
            raise Exception("Indentation can not be decreased to negative values")
        self._indents -= 1

    def calcPrefix(self, log_level=logging.INFO):
        """Calculate the current indentation prefix that should be used.

        Args:
            log_level (enum, optional): logging level, from logging (logging.INFO by default)

        Return Value:
            Indented Meta-sploit style string prefix
        """
        return self._indents * 4 * " " + self._level_masking[log_level] + " "

    def format(self, record):
        """Implement the basic format method.

        Args:
            record (LogRecord): log record to be nicely formatted

        Return Value:
            formated string message that represents the log record
        """
        self_prefix = self.calcPrefix(record.levelno)
        raw_msg  = record.msg
        msg_args = record.args
        record.msg  = ''
        record.args = []
        # We use ColorFormatter (twice) on purpose, as we want to skip forward to it's parent
        prefix = super(ColorFormatter, self).format(record) + self_prefix
        record.msg  = raw_msg
        record.args = msg_args
        # avoid a double prefix
        record.msg  = Logger._fixLines(super(ColorFormatter, self).format(record)[len(prefix) - len(self_prefix):], prefix, is_ui=True)
        record.args = []
        result = super(PrompterFormatter, self).format(record)
        record.msg  = raw_msg
        record.args = msg_args
        return result
