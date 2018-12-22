createAnchor
============
Creates a timestamped output directory for the logs and file outputs of the work script.

Configurations
++++++++++++++

.. attribute:: default_timestamp

   Default timestamp to be used when creating the output directory
   
	"%Y_%m_%d - %H-%M-%S"

Functions
+++++++++

.. function:: createAnchor(base_path, name_format, move_inside = False)

   Creates an anchor directory for the running script's outputs

   :param base_path: (str): basic FS path in which the anchor directory will be created
   :param name_format: (str): name format for the created anchor, expects an "%s" for the generated timestamp
   :param move_inside: (bool, optional): True iff should move the current directory to the anchor (False by default)
   :return: absolute path to the created anchor directory