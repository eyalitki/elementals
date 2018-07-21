import sys
import time
from colorama import init

# Init the colorama state
init()

class StatusBar(object):
    """Status Bar utility for tasks without a known size limit

    Attributes:
        _messasge (str): message that should be used when printting the status
        _time_format (str): time format to be used for the elapsed time (None if time is not to be printted)
        _num_spaces (int): number of spaces that should be used before the format message is printted
        _refresh_period (int) : time period (in seconds) used to update the shown status, or -1 if not activated
        _last_update (time) : time point of last shown status (None if did not start yet)
        _animation_index (int) : numeric state of the animation
        _animation_states (tuple) : tuple of strings that will be printted one in each state in a cyclic fashion

    Configuration Attributes:
        default_animation (tuple) : tuple of strings that will be printted one in each state in a cyclic fashion
    """

    default_animation = ('-', '\\', '|', '/')

    def __init__(self, message, num_spaces, time_format = None, refresh_interval = 0.5, animation = default_animation):
        """Configures the newly built status bar instance

        Args:
            message (str): message that should be used when printting the status
            num_spaces (int): number of spaces that should be used before the message is printted
            time_format (str, optional) : time format to be used for the elapsed time (None by default)
            refresh_interval (int, optional): time period (in seconds) used to update the shown status, or -1 if not activated. (1 By default)
            animation (tuple, optional): tuple of strings that will be printted one in each state in a cyclic fashion (default_animation by default)
        """
        self._message          = message
        self._time_format      = time_format
        self._num_spaces       = num_spaces
        self._refresh_period   = refresh_interval
        self._last_update      = None
        self._animation_index  = 0
        self._animation_states = animation
        self._start_time       = 0

    def start(self):
        """Marks the start of the progress bar"""
        if self._time_format is not None and self._start_time == 0:
            self._start_time = time.time()
        self.update(True)

    def update(self, force_print = False):
        """An update attempt to the shown status bar

        Args:
            force_print (bool, optional): True iff should force an update of the printted message (False by default)
        """
        # Check if needs to preform an update
        current_time = time.time()
        if force_print or self._refresh_period < 0 or self._last_update is None or current_time - self._last_update >= self._refresh_period:
            self.printStatus()
            # Update the timer
            self._last_update = current_time

    def printStatus(self):
        """Prints the status bar + animation"""

        CURSOR_UP_ONE = "\x1b[1A"
        ERASE_LINE    = "\033[K"

        if self._time_format is not None:
            elapsed_time = time.time() - self._start_time
            time_format = time.strftime(self._time_format, time.gmtime(elapsed_time)) + ' '
        else:
            time_format = ''

        status_line = ' ' * self._num_spaces + time_format + self._message + ' ' + self._animation_states[self._animation_index]
        self._animation_index = (self._animation_index + 1) % len(self._animation_states)
        # Now actually print it
        if self._last_update is not None:
            sys.stdout.write(CURSOR_UP_ONE + ERASE_LINE)
        print(status_line)

    def finish(self):
        """Close the status bar (on error / successful finish)"""
        # Print a final status if one is needed
        self.update(True)
