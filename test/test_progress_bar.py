from elementals import ProgressBar
import time

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
