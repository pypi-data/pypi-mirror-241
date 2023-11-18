#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script for the device MBW973
"""

import logging
from time import sleep

from hvl_ccb.dev.mbw973 import MBW973

logging.basicConfig(level=logging.INFO)

# create device object
mbw = MBW973({"port": "COM3"})

# start the device
mbw.start()

# start dew point control to generate a new measurement sample
mbw.start_control()

# wait until done
while not mbw.is_done_with_measurements:
    sleep(1)

# get results and print them
results = mbw.read_measurements()
print(results)
