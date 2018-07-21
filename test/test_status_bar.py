from elementals	import StatusBar
import time

s = StatusBar('Searching for the ELF\'s start', 30, time_format = "Elapsed %M:%S -")
s.start()
for i in xrange(100) :
	s.update( )
	time.sleep(0.1)
s.finish( )
