import time
import os

default_timestamp = "%Y_%m_%d - %H-%M-%S"

def createAnchor(base_path, name_format, move_inside = False):
    """Creates an anchor directory for the running script's outputs

    Args:
        base_path (str): basic FS path in which the anchor directory will be created
        name_format (str): name format for the created anchor: (timestamp)
        move_inside (bool, optional): True iff should move the current directory to the anchor (False by default)

    Return Value:
        absolute path to the created anchor directory
    """

    abs_base = os.path.abspath(base_path)
    anchor_dir = name_format % time.strftime(default_timestamp)
    abs_anchor = os.path.join(abs_base, anchor_dir)
    os.mkdir(abs_anchor)
    if move_inside:
        os.chdir(abs_anchor)
    return abs_anchor
