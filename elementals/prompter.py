from logger import Logger
from colorama import Style

class Prompter(Logger):
    """Exploit oriented cmd prompter, uses logger behind the scenes

    Attributes:
        _logger (logger): inner logger that logs the actions to files (different format than stdout)
        _level_masking (dict) : mapping between the logger's levels and the shown levels
        _indents (int): indentation level
    """

    def __init__(self, log_file_names, min_log_level = Logger.EVENT_LEVEL, timestamp = Logger.default_timestamp, log_format = Logger.default_log_format, log_types = Logger.default_types):
        """Configures the newly built logger instance

        Args:
            log_files (tuple of tuples): tuple of log files we should use: (log file name, open mode)
            min_log_level (enum, optional): minimum log level. Value should be an enum option from the log level names (EVENT_LEVEL by default)
            timestamp (str, optional): time format to be used in every log record (default_timestamp by default)
            log_format (str, optional): overall format of the log records (default_log_format by default)
            log_types (tuple, optional): orderred tuple (ascending importance order) of (<log level name (str)>, <colorama formatting>) (default_types by default)
        """
        self._logger         = Logger(log_file_names, use_stdout = False, min_log_level = min_log_level, timestamp = timestamp, log_format = log_format, log_types = log_types)
        self._level_masking  = { Logger.DEBUG_LEVEL  : '[$]', 
                                 Logger.EVENT_LEVEL  : '[+]',
                                 Logger.WARNING_LEVEL: '[*]',
                                 Logger.ERROR_LEVEL:   '[!]',
                               }
        self._indents        = 0

    def addIndent(self):
        self._indents += 1

    def removeIndent(self):
        if self._indents <= 0:
            raise Exception("Indentation can not be decreased to negative values")
        self._indents -= 1

    def logMessage(self, message, log_level = Logger.EVENT_LEVEL):
        """Logs the message (to a file) and prompts it using stdout

        Args:
            message (str): Log record description
            log_level (enum, optional): Log level for the message (EVENT_LEVEL by default)
        """
        self._logger.logMessage(message, log_level)

        # Check the minimal level
        if self._logger._log_levels[log_level] < self._logger._min_level :
            return

        log_style = self._logger._log_styles[log_level]
        log_level = self._level_masking[log_level]
        out_format = " " * 4 * self._indents + " %s %s"

        # Check if we have a multilined message
        if '\n' in message:
            # measure the size of the format
            template_record = out_format % (log_level, "")

            message_parts = message.split('\n')
            msg_record = template_record + message_parts[0] + '\n'
            for part in message_parts[1:]:
                msg_record += template_record + part + '\n'
            msg_record = msg_record[:-1]

        else:
            # Build up the full message format
            msg_record = out_format % (log_level, message)

        # Now print it to the standard output
        print(log_style + msg_record + Style.RESET_ALL)
