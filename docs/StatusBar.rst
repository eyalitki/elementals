StatusBar
=========
Status Bar utility for tasks without a known size limit

Attributes
++++++++++

.. attribute:: StatusBar.default_animation

    tuple of strings that will be printed one in each state in a cyclic fashion::
   
	('-', '\\', '|', '/')

Functions
+++++++++

.. function:: StatusBar.__init__(self, message, num_spaces, time_format = None, refresh_interval = 0.5, animation = default_animation)

   Configures the newly built status bar instance

   :param message: (str): message that should be used when printing the status
   :param num_spaces: (int): number of spaces that should be used before the message is printed
   :param time_format: (str, optional) : time format to be used for the elapsed time (None by default)
   :param refresh_interval: (int, optional): time period (in seconds) used to update the shown status, or -1 if not activated. (0.5 by default)
   :param animation: (tuple, optional): tuple of strings that will be printed one in each state in a cyclic fashion (default_animation by default)
   
.. function:: StatusBar.start(self)

   Marks the start of the progress bar

.. function:: StatusBar.update(self, force_print = False)

   An update attempt to the shown status bar

   :param force_print: (bool, optional): True iff should force an update of the printed message (False by default)
   
.. function:: StatusBar.printStatus(self)

   Prints the status bar + animation

.. function:: StatusBar.finish(self)

   Close the status bar (on error / successful finish)