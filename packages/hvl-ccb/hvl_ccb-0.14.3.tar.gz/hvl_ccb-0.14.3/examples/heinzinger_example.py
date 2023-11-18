#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script for the device Heinzinger
"""

import logging
from time import sleep

from hvl_ccb.dev.heinzinger import Heinzinger

logging.basicConfig(level=logging.INFO)

# create device object
hv = Heinzinger({"port": "COM5"})

# start the device
hv.start()

# give the device some time to apply hv.set_number_of_recordings()
# that was called during hv.start()
sleep(0.5)

# print the nominal voltage and current
print(
    f"This power supply can apply {hv.max_voltage_hardware} V"
    f" and {hv.max_current_hardware} A"
)

# restrict the maximum voltage and current to lower values
hv.max_voltage = 1_200
hv.max_current = 0.5e-3
# will raise ValueError if the user attempts to set a higher value

# apply the current limitation
hv.current = hv.max_current
sleep(0.5)

# turn on the output
hv.output = True
sleep(0.5)

try:
    hv.voltage = 1_300
except ValueError:
    print(f"You can't set a voltage higher than {hv.max_voltage} V.")

# sleep(1)
# apply a voltage
set_voltage = 1_106
hv.voltage = set_voltage
sleep(0.5)  # give the device some time to apply hv.set_voltage()

# check the set voltage
command_voltage = hv.voltage

sleep(10)  # give the device some time to step up the output voltage

# measure the output voltage
meas_voltage = hv.set_voltage

# print the result
print(
    f"I wanted to set {set_voltage} V, "
    f"the command set {command_voltage} V, "
    f"and I measured {meas_voltage} V"
)

# stop the device (this also turns off the output)
hv.stop()
