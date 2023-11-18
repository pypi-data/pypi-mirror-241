#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script for the device Elektro Automatik PSI 9080-2040 power supply.
"""

import logging
from time import sleep

from hvl_ccb.comm.visa import VisaCommunication, VisaCommunicationConfig
from hvl_ccb.dev.ea_psi9000 import PSI9000

logging.basicConfig(level=logging.INFO)

# configuration dict with appropriate settings
com_config = {
    "interface_type": VisaCommunicationConfig.InterfaceType.TCPIP_SOCKET,
    "board": 0,
    "host": "192.168.1.31",
    "port": 5025,
}

# create communication protocol object
com_device = VisaCommunication(com_config)

# create device object
psi9080_2040 = PSI9000(com_device)
psi9080_2040.start()

# go into remote mode by locking
psi9080_2040.set_system_lock(True)

# get IDN and print it
psi9080_2040.get_identification()

# check master slave config, INIT if necessary
psi9080_2040.check_master_slave_config()

# set upper and lower U and I limits
psi9080_2040.set_upper_limits(voltage_limit=80, current_limit=2040)
psi9080_2040.set_lower_limits(voltage_limit=0, current_limit=0)

# set U and I setpoint
psi9080_2040.set_voltage_current(10, 2000)

# enable output
psi9080_2040.set_output(True)

sleep(2)

# measure voltage and current at the output
volt, current = psi9080_2040.measure_voltage_current()

sleep(2)

# disable the output
psi9080_2040.set_output(False)
sleep(2)

# shut down device
psi9080_2040.stop()
