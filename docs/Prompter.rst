Prompter
========
Exploit oriented cmd prompter, uses logger behind the scenes

Configurations
++++++++++++++

.. attribute:: PrompterFormatter.default_level_masking

   Default metasploit-style prefix for each logging level::
   
	logging.DEBUG      ==> '[$]'
   
	logging.INFO       ==> '[+]'
   
	logging.WARN       ==> '[*]'
   
	logging.ERROR      ==> '[!]'
   
	logging.CRITICAL   ==> '[!]'

Functions
+++++++++

.. function:: Prompter.__init__(self, name='', log_file_names=[], min_log_level=logging.INFO, timestamp=Logger.default_timestamp, log_format=Logger.default_log_format)

   Configures the newly built prompter instance

   :param name: (str, optional): name of the logger instance (no name by default)
   :param log_files: (tuple of tuples, optional): tuple of log files we should use: (log file name, open mode (, min log level))
   :param min_log_level: (enum, optional): minimum log level. Value should be an enum option from the log level names (logging.INFO by default)
   :param timestamp: (str, optional): time format to be used in every log record (default_timestamp by default)
   :param log_format: (str, optional): overall format of the log records (default_log_format by default)

.. function:: Prompter.setPrefix(self, log_level, prefix)

   Updates the basic style for a specific logging level

   :param log_level: (enum): logging level (from logging)
   :param prefix: (style): string prefix for the desired logging level
   
.. function:: Prompter.setColor(self, log_level, style)

   Updates the basic style for a specific logging level in the StreamHandler
   
   :param log_level: (enum): logging level (from logging)
   :param style: (style): colorama style for the desired logging level
   
.. function:: Prompter.addIndent(self)

   Adds an indentation level to the following log records shown on the stdout
   
.. function:: Prompter.removeIndent(self)

   Removes an indentation level from the following log records shown on the stdout
   
.. function:: Prompter.input(self, msg)

   Prompts the user for a given input, using the same meta-sploit styled prefix

   :param msg: (str): message that would be shown to the user when asking for his input
   :return: User input string, as returned by "raw_input"
   
Usage Examples
++++++++++++++

Creating a basic prompter that prints to the screen:
  .. code-block:: python

   logger = Prompter("Dummy Prompter")
   logger.debug("Debug message that no one will see")
   logger.info("Logging has began")
   logger.addIndent()
   logger.warning("You previous debug message went to /dev/null")
   logger.removeIndent()
   logger.error("This example just ended")

And the output will be:
::
  [+] Logging has began
      [*] You previous debug message went to /dev/null
  [!] This example just ended

Creating a complex logger with multiple files:
  .. code-block:: python

   logger = Prompter("Complex Prompter", [('full_log.txt', 'w', logging.DEBUG)], min_log_level=logging.WARNING)
   logger.debug("Debug message that will be written to the log file")
   logger.info("Logging has began but you won't see it")
   logger.warning("The script is nearing it's end")
   logger.error("This example just ended")

And the output will be:
::
  [*] The script is nearing it's end
  [!] This example just ended
  
And the file log will be:
::
  [14/03/2019 20:08:29] - Complex Prompter - DEBUG: Debug message that will be written to the log file
  [14/03/2019 20:08:29] - Complex Prompter - INFO: Logging has began but you won't see it
  [14/03/2019 20:08:29] - Complex Prompter - WARNING: The script is nearing it's end
  [14/03/2019 20:08:30] - Complex Prompter - ERROR: This example just ended