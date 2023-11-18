#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script to demonstrate the capabilities of the PICube device with
Power Inverter and 50 kV AC Power Setup
"""

import logging
from time import sleep

from hvl_ccb.dev.cube import PICube

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(asctime)s [%(name)s.%(funcName)s] %(message)s",
)

# TWO different approaches to filter unwanted logging messages

# set opcua logging level to WARNING
# to avoid frequent "received header" INFO level log entries,
# if you want to receive the messages you need to decrease the logging level
logging.getLogger("asyncua").setLevel(logging.WARNING)

# alternatively, uncomment the snippet below
# filter out all log entries except the hvl_ccb ones,
# you will see NO messages from any other package
# for handler in logging.root.handlers:
#     handler.addFilter(logging.Filter("hvl_ccb"))

# create a cube object
cube = PICube({"host": "192.168.1.1"})

# start device
cube.start()

# go ready (switch to red state)
cube.ready = True

sleep(5)

# no we can go to operate and switch on HV
cube.operate = True
sleep(5)

print(f"Voltage max returns {cube.voltage_max}")
print(f"Power setup returns {cube.power_setup.name}")

# set test parameters
# cube.set_test_parameters(target_voltage=10_000, slope=2_000)
cube.test_parameter.voltage = 10_000
cube.test_parameter.slope = 2_000
sleep(10)
# cube.get_test_parameters()
print(f"Test parameter voltage returns {cube.test_parameter.voltage}")
print(f"Test parameter slope returns {cube.test_parameter.slope}")

print(f"Actual voltage returns {cube.voltage_actual}")
print(f"Channel 1 measurement voltage returns {cube.measurement_ch_1.voltage}")
print(f"Channel 1 measurement ratio returns {cube.measurement_ch_1.ratio}")
print(f"Channel 3 measurement voltage returns {cube.measurement_ch_3.voltage}")
print(f"Channel 3 measurement ratio returns {cube.measurement_ch_3.ratio}")
print(f"Primary voltage returns {cube.voltage_primary}")
print(f"Primary current returns {cube.current_primary}")
print(f"Frequency returns {cube.frequency}")

# cube.set_test_parameters(target_voltage=0, slope=5_500)
cube.test_parameter.voltage = 0
cube.test_parameter.slope = 5_500


sleep(5)

print(f"Fast switch off triggered returns {cube.breakdown_detection_triggered}")
print(f"Fast switch off active returns {cube.breakdown_detection_active}")
cube.breakdown_detection_reset()


# switch HV off
cube.operate = False

sleep(5)

# and go back to green
cube.ready = False
sleep(5)

# stop device
cube.stop()
