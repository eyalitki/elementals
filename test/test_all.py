from elementals import ProgressBar
from elementals	import StatusBar
from elementals	import Prompter
from elementals	import createAnchor
import time

createAnchor(".", "Output %s", move_inside = True)

prompt = Prompter([('action_log.txt', 'w')])
prompt.logEvent("Started the script")
prompt.logEvent("Phase #1 - collecting the data")
prompt.addIndent()
prompt.logEvent("Searching for the tool")

s = StatusBar('Searching for the ELF\'s start', 30, time_format = "Elapsed %M:%S -")
s.start()
for i in xrange(100) :
	s.update( )
	time.sleep(0.1)
s.finish( )

prompt.logWarning("The tool only supports 32 bit")

prompt.logEvent("Activating the tool")

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
prompt.logEvent("Successful finish")