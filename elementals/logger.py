import time
from colorama import init, Fore, Style

# Init the colorama state
init()

class Logger(object):
    """Generic Logger that prints both to stdout and an external log file

    Attributes:
        _timestamp  (str): time stamp that is used for the log records
        _log_format (str): record log format using the following arguments: (timestamp, log type, log message)
        _log_types  (tuple of tuples): orderred in ascending importance order (<log level name (str)>, <colorama formatting>)
        _log_files  (list of fds): tuple of opened log files descriptors
        _use_stdout (boolean): True iff we should also print to stdout
        _min_level (enum): minimal logging level that should be recorded 
        _log_levels (dict): a mapping between a log level's name and its importance index
        _log_styles (dict): a mapping between a log level's name and its style

    Configurations:
        default_timestamp  (str): Default time stamp that is used for the log records
        default_log_format (str): Default record log format: (timestamp, log type, log message)
                                  NOTE: multiline comments assume that the message ends the record's line
        default_types      (tuple of tuples): orderred in ascending importance order (<log level name (str)>, <colorama formatting>)
    """

    default_timestamp   = "%d/%m/%Y %H:%M:%S"
    default_log_format  = "[%s] - %s: %s"

    DEBUG_LEVEL         = 'DEBUG'
    EVENT_LEVEL         = 'EVENT'
    WARNING_LEVEL       = 'WARNING'
    ERROR_LEVEL         = 'ERROR'

    default_types       = ((DEBUG_LEVEL,   Fore.LIGHTCYAN_EX), 
                           (EVENT_LEVEL,   Fore.LIGHTWHITE_EX),
                           (WARNING_LEVEL, Fore.LIGHTYELLOW_EX),
                           (ERROR_LEVEL,   Fore.LIGHTRED_EX),
                          )

    def __init__(self, log_file_names, use_stdout = True, min_log_level = EVENT_LEVEL, timestamp = default_timestamp, log_format = default_log_format, log_types = default_types):
        """Configures the newly built logger instance

        Args:
            log_files (tuple of tuples): tuple of log files we should use: (log file name, open mode)
            use_stdout (boolean, optional): should we print to stdout? (True by default)
            min_log_level (enum, optional): minimum log level. Value should be an enum option from the log level names (EVENT_LEVEL by default)
            timestamp (str, optional): time format to be used in every log record (default_timestamp by default)
            log_format (str, optional): overall format of the log records (default_log_format by default)
            log_types (tuple, optional): orderred tuple (ascending importance order) of (<log level name (str)>, <colorama formatting>) (default_types by default)

        """
        self._timestamp  = timestamp
        self._log_format = log_format
        self._log_types  = log_types
        self._use_stdout = use_stdout
        self._min_level  = min_log_level
        self._log_files  = []
        for file_name, open_mode in log_file_names:
            self._log_files.append(open(file_name, open_mode))

        # Build up the importance mapping
        self._log_levels = {}
        self._log_styles = {}
        counter = 0
        for level_name, level_style in log_types:
            self._log_levels[level_name] = counter
            self._log_styles[level_name] = level_style
            counter += 1

        # Verify that the minimal level is valid
        if self._min_level not in self._log_levels:
            raise Exception("Minimal Logging level \"%s\" is Invalid, not in log types options..." % self._min_level)
        self._min_level = self._log_levels[self._min_level]

    def addIndent(self):
        """Adds an indentation level to the following log records shown on the stdout"""
        pass

    def removeIndent(self):
        """Removes an indentation level from the following log records shown on the stdout"""
        pass

    def logDebug(self, message):
        """Logs the message using the default DEBUG level

        Args:
            message (str): Log record description
        """
        self.logMessage(message, self.DEBUG_LEVEL)

    def logEvent(self, message):
        """Logs the message using the default EVENT level

        Args:
            message (str): Log record description
        """
        self.logMessage(message, self.EVENT_LEVEL)

    def logWarning(self, message):
        """Logs the message using the default WARNING level

        Args:
            message (str): Log record description
        """
        self.logMessage(message, self.WARNING_LEVEL)

    def logError(self, message):
        """Logs the message using the default ERROR level

        Args:
            message (str): Log record description
        """
        self.logMessage(message, self.ERROR_LEVEL)

    def logMessage(self, message, log_level = EVENT_LEVEL):
        """Logs the message according to the specified logging level

        Args:
            message (str): Log record description
            log_level (enum, optional): Log level for the message (EVENT_LEVEL by default)
        """

        # Check that the log level is valid
        if log_level not in self._log_levels:
            raise Exception("Unknown log level: \"%s\"" % log_level)

        # Check the minimal level
        if self._log_levels[log_level] < self._min_level :
            return

        # Check if we have a multilined message
        if '\n' in message:
            # measure the size of the format
            template_record = self._log_format % (time.strftime(self._timestamp), log_level, "")
            fixed_start = " " * len(template_record)

            message_parts = message.split('\n')
            msg_record = template_record + message_parts[0] + '\n'
            for part in message_parts[1:]:
                msg_record += fixed_start + part + '\n'
            msg_record = msg_record[:-1]

        else:
            # Build up the full message format
            msg_record = self._log_format % (time.strftime(self._timestamp), log_level, message)

        for fd in self._log_files :
            fd.write(msg_record + '\n')
            fd.flush()

        # Now check the standard output
        if self._use_stdout:
            print(self._log_styles[log_level] + msg_record + Style.RESET_ALL)
