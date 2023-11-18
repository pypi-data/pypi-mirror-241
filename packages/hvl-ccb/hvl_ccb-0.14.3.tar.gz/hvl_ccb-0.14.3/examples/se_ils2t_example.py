#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script for the device Schneider Electric ILS2T stepper motor.
"""

import logging

from hvl_ccb.comm.modbus_tcp import ModbusTcpCommunication
from hvl_ccb.dev.se_ils2t import ILS2T

logging.basicConfig(level=logging.INFO)

# configuration dict with appropriate settings
com_config = {
    "host": "192.168.1.51",
    "unit": 255,
}

# create communication protocol object
com_device = ModbusTcpCommunication(com_config)

# create device object
ils2t = ILS2T(com_device)

# start the device
ils2t.start()

ils2t.execute_relative_step(10 * 16_000)

print(f"Position: {ils2t.get_position()}")
print(f"Temperature: {ils2t.get_temperature()} °C")
print(f"DC Voltage: {ils2t.get_dc_volt()} V")
print(f"Status: {ils2t.get_status()}")

ils2t.execute_relative_step(-10 * 16_000)
print(f"Position: {ils2t.get_position()}")

ils2t.execute_absolute_position(10_000)
print(f"Position: {ils2t.get_position()}")

ils2t.execute_absolute_position(0)
print(f"Position: {ils2t.get_position()}")

ils2t.stop()
