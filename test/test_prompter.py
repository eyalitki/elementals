from elementals import ProgressBar
from elementals	import Prompter
import time
import logging

TOOL_NAME = "Extractor"

prompt = Prompter("test", [('action_log.txt', 'w', logging.DEBUG)])
prompt.debug("The name should be \"test\"")
prompt.info("Started the script")
prompt.info("Phase #1 - collecting the data")
prompt.addIndent()
prompt.info("Activating tool %s" , TOOL_NAME)
p = ProgressBar('Leaked %3d / %3d bytes - %3d%% Completed', 250, 30, True, time_format = "Elapsed %M:%S -")
p.start( )
p.advance( 1 )
time.sleep( 2 )
p.advance( 50 )
time.sleep( 1.5 )
p.advance( 100 )
time.sleep( 2 )
p.advance( 1 )
time.sleep( 0.5 )
p.advance( 200 )
p.finish( )
prompt.removeIndent()
prompt.info("Successful finish")