'''
Created on Apr 15, 2016

@author: lukasz-filiks
'''

import time

LED3_PATH = "/sys/class/leds/beaglebone:green:usr3"

for i in range(0, 10):
    
    f = open(LED3_PATH + "/brightness","w")
    f.write(1)
    f.close()
    
    time.sleep(1)
    
    f = open(LED3_PATH + "/brightness","w")
    f.write(0)
    f.close()
    
    time.sleep(1)

exit(0)
