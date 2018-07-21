from elementals import ProgressBar
from elementals import StatusBar
from elementals	import Prompter
from elementals import createAnchor

import time
import logging

createAnchor(".", "Output %s", move_inside = True)

prompt = Prompter("test", [('action_log.txt', 'w', logging.DEBUG)])
prompt.debug("The name should be \"test\"")
prompt.info("Started the script")
prompt.info("Phase #1 - collecting the data")
prompt.addIndent()
prompt.info("Searching for the tool")

s = StatusBar('Searching for the ELF\'s start', 30, time_format = "Elapsed %M:%S -")
s.start()
for i in xrange(100) :
	s.update( )
	time.sleep(0.1)
s.finish( )

prompt.warning("The tool only supports 32 bit")

prompt.info("Activating the tool")

p = ProgressBar('Leaked %3d / %3d bytes - %3d%% Completed', 250, 30, True, time_format = "Elapsed %M:%S -")
p.start( )
p.advance( 1 )
time.sleep(2)
p.advance( 50 )
time.sleep(1.5)
p.advance( 100 )
time.sleep(2)
p.advance( 1 )
time.sleep(0.5)
p.advance( 200 )
p.finish( )

prompt.removeIndent()
prompt.info("Successful finish")