import sys
import time
from colorama import init

# Init the colorama state
init()

class ProgressBar(object):
    """Progress Bar utility for tasks with a known size limit

    Attributes:
        _format (str): format string (work done, total work, percentage) to be used for the printted message
        _time_format (str): time format to be used for the elapsed time (None if time is not to be printted)
        _num_spaces (int): number of spaces that should be used before the format message is printted
        _work_done (int): amount of work that was done till now
        _total_work (int): overall amount of work that needs to be done
        _use_bar (bool) : True iff there should be printted also a graphical status bar
        _refresh_period (int) : time period (in seconds) used to update the shown status, or -1 if not activated
        _last_update (time) : time point of last shown status (None if did not start yet)
        _start_time (int) : time point of the progress start
    """

    def __init__(self, progress_format, total_work, num_spaces, use_bar = False, time_format = None, refresh_interval = 1):
        """Configures the newly built progress bar instance

        Args:
            progress_format (str): format string (work done, total work, percentage) to be used for the printted message
            total_work (int): total amount of work to be done (in some measuring unit)
            num_spaces (int): number of spaces that should be used before the format message is printted
            use_bar (bool, optional): True iff should also print a graphical status bar (False by default)
            time_format (str, optional) : time format to be used for the elapsed time (None by default)
            refresh_interval (int, optional): time period (in seconds) used to update the shown status, or -1 if not activated. (1 By default)
        """
        self._format         = progress_format
        self._time_format    = time_format
        self._num_spaces     = num_spaces
        self._work_done      = 0
        self._total_work     = total_work
        self._use_bar        = use_bar
        self._refresh_period = refresh_interval
        self._last_update    = None
        self._start_time     = 0

    def start(self):
        """Marks the start of the progress bar"""
        if self._time_format is not None and self._start_time == 0:
            self._start_time = time.time()
        self.update(True)

    def advance(self, units, force_print = False):
        """Marks the completion of X units of work

        Args:
            units (int): Number of units of work that were finished
            force_print (bool, optional): True iff should force an update of the printted message (False by default)
        """
        self._work_done += units
        self._work_done = min(self._work_done, self._total_work)
        self.update(force_print)

    def update(self, force_print = False):
        """An update attempt to the shown progress status

        Args:
            force_print (bool, optional): True iff should force an update of the printted message (False by default)
        """
        # Check if needs to preform an update
        current_time = time.time()
        if force_print or self._refresh_period < 0 or self._last_update is None or current_time - self._last_update >= self._refresh_period:
            self.printProgress()
            # Update the timer
            self._last_update = current_time

    def printProgress(self):
        """Prints the progress status + progress bar"""

        CURSOR_UP_ONE = "\x1b[1A"
        ERASE_LINE    = "\033[K"

        work_percentage = (self._work_done * 1.0 / self._total_work)
        if self._time_format is not None:
            elapsed_time = time.time() - self._start_time
            time_format = time.strftime(self._time_format, time.gmtime(elapsed_time)) + ' '
        else:
            time_format = ''
        status_line = ' ' * self._num_spaces + time_format + self._format % (self._work_done, self._total_work, int(100 * work_percentage))
        if self._use_bar:
            line_size = len(status_line)
            progress_bar = '=' * int(work_percentage * line_size)
            progress_bar += ' ' * (line_size - len(progress_bar))
            progress_line = ' ' * (self._num_spaces / 2) + '[%s]' % progress_bar
        # Now actually print it
        if self._last_update is not None:
            if self._use_bar:
                sys.stdout.write(CURSOR_UP_ONE + ERASE_LINE)
            sys.stdout.write(CURSOR_UP_ONE + ERASE_LINE)
        print(status_line)
        if self._use_bar:
            print(progress_line)

    def finish(self):
        """Close the progress bar (on error / successful finish)"""
        # Print a final status if one is needed
        self.update(self._work_done == self._total_work)
        # restore the stdout position
        print('')
