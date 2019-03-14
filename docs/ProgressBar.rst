ProgressBar
===========
Progress Bar utility for tasks with a known size limit

Functions
+++++++++

.. function:: ProgressBar.__init__(self, progress_format, total_work, num_spaces, use_bar=False, time_format=None, refresh_interval=1)

   Configures the newly built progress bar instance

   :param progress_format: (str): format string (work done, total work, percentage) to be used for the printed message
   :param total_work: (int): total amount of work to be done (in some measuring unit)
   :param num_spaces: (int): number of spaces that should be used before the format message is printed
   :param use_bar: (bool, optional): True iff should also print a graphical status bar (False by default)
   :param time_format: (str, optional) : time format to be used for the elapsed time (None by default)
   :param refresh_interval: (int, optional): time period (in seconds) used to update the shown status, or -1 if not activated. (1 by default)
   
.. function:: ProgressBar.start(self)

   Marks the start of the progress bar
   
.. function:: ProgressBar.advance(self, units, force_print=False)

   Marks the completion of X units of work

   :param units: (int): Number of units of work that were finished
   :param force_print: (bool, optional): True iff should force an update of the printed message (False by default)

.. function:: ProgressBar.update(self, force_print=False)

   An update attempt to the shown progress status

   :param force_print: (bool, optional): True iff should force an update of the printed message (False by default)
   
.. function:: ProgressBar.printProgress(self)

   Prints the progress status + progress bar

.. function:: ProgressBar.finish(self)

   Close the progress bar (on error / successful finish)
   
Usage Examples
++++++++++++++

Creating a classic progress bar that advances randomly:
  .. code-block:: python
  
   p = ProgressBar('Leaked %3d / %3d bytes - %3d%% Completed', 250, 30, True, time_format="Elapsed %M:%S -")
   p.start()
   p.advance(1)
   time.sleep(2)
   p.advance(50)
   time.sleep(1.5)
   p.advance(100)
   time.sleep(2)
   p.advance(1)
   time.sleep(0.5)
   p.advance(200)
   p.finish()