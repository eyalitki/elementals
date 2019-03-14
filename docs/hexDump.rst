hexDump
=======
Prints the given input as a hex-editor style string

Functions
+++++++++

.. function:: hexDump(data)

   Prepares a hexdump string to be nicely printed by a logger

   :param data: (str): binary blob to be converted to a nice hexdump
   :return: hexdump formatted string (possibly with multiple lines)
   
Usage Examples
++++++++++++++

Debug logging the hex dump of a compiled shellcode:
  .. code-block:: python

   logger.debug(hexDump(shellcode))