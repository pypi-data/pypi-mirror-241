#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script for the device Lauda PRO RP245E.
"""

import logging
import time

from hvl_ccb.dev.lauda import LaudaProRp245e, LaudaProRp245eTcpCommunication

logging.basicConfig(level=logging.INFO)

# configuration dict with appropriate settings
com_config = {
    "host": "192.168.0.5",
    "port": 54321,
}

# create communication protocol object
com_device = LaudaProRp245eTcpCommunication(com_config)

# create device object
rp245 = LaudaProRp245e(com_device)

# start the device
rp245.start()

# Test communication: ask the device to return its device type and print out the answer
print(rp245.get_device_type())

# Read and print bath temperature
print("The bath temperature currently is: ", rp245.get_bath_temp())

# Set target bath-temperature to 10°C
rp245.set_temp_set_point(10)

# Set pump level (strength) to 2
rp245.set_pump_level(2)

# Run cooling for 30 seconds, then pause
"""
Caution! This will activate the chilling unit and the pump!
Uncomment run-command only when hoses are connected to the input/output ports for the
cooling liquid!
"""
rp245.run()
time.sleep(30)
rp245.pause()

# Stop operation and shut down connection
rp245.stop()
