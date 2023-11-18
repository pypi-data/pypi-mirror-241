#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script to demonstrate the capabilities of the BaseCube device.
"""

import logging
from time import sleep

from hvl_ccb.dev.cube import BaseCube, constants, earthing_stick

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)40s %(levelname)8s %(message)s",
)

# TWO different approaches to filter unwanted logging messages

# set asyncua (interface to opc) logging level to WARNING
# to avoid frequent "received header" INFO level log entries,
# if you want to receive the messages you need to decrease the logging level
logging.getLogger("asyncua").setLevel(logging.WARNING)

# alternatively, uncomment the snippet below
# filter out all log entries except the hvl_ccb ones,
# you will see NO messages from any other package
# for handler in logging.root.handlers:
#     handler.addFilter(logging.Filter("hvl_ccb"))


# cube = BaseCube({'host': '172.31.27.45'})
cube = BaseCube({"host": "192.168.1.1"})

cube.start()


cube.support_1.output_1 = True
print(f"Support output port 1 contact 1 returns {cube.support_1.output_1}")
sleep(0.5)
cube.support_1.output_1 = False
print(f"Support output port 1 contact 1 returns {cube.support_1.output_1}")
sleep(0.5)

print(f"Support input port 1 contact 1 returns {cube.support_1.input_1}")


# loop through T13 sockets and switch them on and off
cube.t13_socket_1 = True
print(f"T13 socket 1 returns {cube.t13_socket_1}")
sleep(1)
cube.t13_socket_1 = False
print(f"T13 socket 1 returns {cube.t13_socket_1}")
sleep(0.5)
# switch on and off CEE16 socket
cube.cee16_socket = True
print(f"CEE16 socket returns {cube.cee16_socket}")
sleep(1)
cube.cee16_socket = False
print(f"CEE16 socket returns {cube.cee16_socket}")
sleep(1)

# safety circuit: first go into ready state, but before wait until we can go ready
while cube.status is not constants.SafetyStatus.GREEN_READY:
    sleep(1)


print(f"Door 1 status returns {cube.door_1_status}")
print(f"Earthing rod 1 status returns {cube.earthing_rod_1_status}")
print(f"Earthing stick 1 status returns {cube.earthing_stick_1.status}")

cube.ready = True

sleep(5)

while cube.status is not constants.SafetyStatus.RED_READY:
    sleep(1)

# no we can go to operate and switch on HV
cube.operate = True
sleep(5)

cube.earthing_stick_1.operate = earthing_stick.SwitchOperation.CLOSE
print(f"Earthing stick 1 manual returns {cube.earthing_stick_1.manual}")
sleep(10)
cube.earthing_stick_1.operate = earthing_stick.SwitchOperation.OPEN
print(f"Earthing stick 1 manual returns {cube.earthing_stick_1.manual}")

cube.quit_error()

cube.operate = False
cube.ready = False


print(f"Measurement ratio channel 1 returns {cube.measurement_ch_1.ratio}")
print(f"Measurement voltage channel 1 returns {cube.measurement_ch_1.voltage}")
# Test Status
cube.set_status_board(["Hello World", "Hello Fabian", "Hello HVL"], [4, 8, 12])
cube.set_status_board([str(i) for i in range(0, 15)])
cube.set_message_board([f"{i}: ERROR: This is unexpected" for i in range(0, 15)])
cube.set_message_board(["Good choice"])
cube.display_status_board()
cube.display_message_board()
cube.stop()
