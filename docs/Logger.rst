Logger
======
Wrapper to python's `logging.Logger <https://docs.python.org/2/library/logging.html#logger-objects/>`_, customized to use colors, and set up with pre-defined time stamp values.

Configurations
++++++++++++++

.. attribute:: ColorFormatter.default_colors

   Default color mapping for each logging level::
   
	logging.DEBUG    ==> Fore.LIGHTCYAN_EX
	
	logging.INFO     ==> Fore.LIGHTWHITE_EX
	
	logging.WARN     ==> Fore.LIGHTYELLOW_EX
	
	logging.ERROR    ==> Fore.LIGHTRED_EX
	
	logging.CRITICAL ==> Fore.LIGHTRED_EX

Attributes
++++++++++

.. attribute:: Logger.default_timestamp

   Default value for the log's time stamp: "%d/%m/%Y %H:%M:%S"
   
.. attribute:: Logger.default_log_format

   Default log record format, for a named logger: "[%(asctime)s] - %(name)s - %(levelname)s: %(message)s"
   
.. attribute:: Logger.default_nameless_log_format 

   Default log record format, a nameless logger: "[%(asctime)s] - %(levelname)s: %(message)s"

Functions
+++++++++

.. function:: Logger.__init__(self, name, log_file_names=[], use_stdout=True, min_log_level=logging.INFO, timestamp=default_timestamp, log_format=default_log_format)

   Configures the newly built logger instance

   :param name: (str): name for the logger instance
   :param log_files: (tuple of tuples, optional): tuple of log files we should use: (log file name, open mode (, min log level))
   :param use_stdout: (boolean, optional): should we print to stdout? (True by default)
   :param min_log_level: (enum, optional): minimum log level. Value should be an enum option from the log level names (logging.INFO by default)
   :param timestamp: (str, optional): time format to be used in every log record (default_timestamp by default)
   :param log_format: (str, optional): overall format of the log records (default_log_format by default)
   
.. function:: Logger.linkHandler(self, handler, log_level=None)

   Links an additional custom handler

   :param handler: (logging.Handler): custom handler
   :param log_level: (enum, optional): minimal logging level (self._min_level by default)
   
.. function:: Logger.setColor(self, log_level, style)

   Updates the basic style for a specific logging level in the StreamHandler

   :param log_level: (enum): logging level (from logging)
   :param style: (style): colorama style for the desired logging level
   
.. function:: Logger.addIndent(self)

   Adds an indentation level to the following log records shown on the stdout (only meaningful for Prompter)
   
.. function:: Logger.removeIndent(self)

   Removes an indentation level from the following log records shown on the stdout (only meaningful for Prompter)
   
Usage Examples
++++++++++++++

Creating a basic logger that prints to the screen:
  .. code-block:: python

   logger = Logger("Dummy Logger")
   logger.debug("Debug message that no one will see")
   logger.info("Logging has began")
   logger.warning("You previous debug message went to /dev/null")
   logger.error("This example just ended")

And the output will be:
::
  [14/03/2019 19:55:59] - Dummy Logger - INFO: Logging has began
  [14/03/2019 19:55:59] - Dummy Logger - WARNING: You previous debug message went to /dev/null
  [14/03/2019 19:55:59] - Dummy Logger - ERROR: This example just ended

Creating a complex logger with multiple files:
  .. code-block:: python

   logger = Logger("Complex Logger", [('full_log.txt', 'w', logging.DEBUG), ('warning_log.txt', 'w', logging.WARNING)], min_log_level=logging.DEBUG)
   logger.debug("Debug message that will be seen this time")
   logger.info("Logging has began")
   logger.warning("You previous debug message went to /dev/null")
   logger.error("This example just ended")

And the output will be:
::
  [14/03/2019 19:59:15] - Complex Logger - DEBUG: Debug message that will be seen this time
  [14/03/2019 19:59:15] - Complex Logger - INFO: Logging has began
  [14/03/2019 19:59:15] - Complex Logger - WARNING: You previous debug message went to /dev/null
  [14/03/2019 19:59:17] - Complex Logger - ERROR: This example just ended

