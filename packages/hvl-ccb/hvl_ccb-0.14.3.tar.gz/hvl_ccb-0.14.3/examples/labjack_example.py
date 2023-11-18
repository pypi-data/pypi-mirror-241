#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script for using the LabJack T7 device

To use a LabJack T-series devices wrapper:

1. install the `hvl_ccb` package with a `labjack` extra feature::

        $ pip install "hvl_ccb[labjack]"

   this will install the Python bindings for the library.

2. install the additional system library - follow instruction in
   https://labjack.com/support/software/installers/ljm .
"""

import logging
from time import sleep

from hvl_ccb.comm.labjack_ljm import LJMCommunicationConfig
from hvl_ccb.dev.labjack import LabJack
from hvl_ccb.utils.conversion import Temperature

# configure logger
logging.basicConfig(level=logging.INFO)

# create communication protocol configuration dict
com_config = {
    "device_type": LJMCommunicationConfig.DeviceType.T7,
    "connection_type": LJMCommunicationConfig.ConnectionType.USB,
    "identifier": "ANY",
}

# create device
labj = LabJack(com_config)

# start device, this also opens the port
labj.start()

# get and print the serial number of the connected LabJack device
print(f"SN: {labj.get_serial_number()}")

# print temperature and relative humidity of a connected SBUS sensor
print(
    "Temperature and relative humidity reading from a Labjack EI-1050: \n"
    f"Temperature = {Temperature.convert(labj.get_sbus_temp(0)):.2f} °C \n"
    f"Temperature = {Temperature.convert(labj.get_sbus_temp(0), target='F'):.2f} °F \n"
    f"Relative Humidity = {labj.get_sbus_rh(0):.1f} %"
)

# init a thermocouple and read the value
ain_tc = 0
labj.set_ain_thermocouple(
    ain_tc,
    thermocouple="T",
    cjc_address=4,
    cjc_type="lm34",
    unit="C",
)
print(f"Temperature Thermocouple = {labj.read_thermocouple(ain_tc):.2f} °C")
sleep(0.5)

# init differential analog input
ain_input = 0
labj.set_ain_differential(ain_input, True)
labj.set_ain_range(ain_input, 10)
labj.set_ain_resolution(ain_input, 12)

print(
    f"voltage between input channels {ain_input}/{ain_input + 1}: "
    f"{(labj.get_ain(ain_input)):.2f} V"
)
sleep(0.5)

print(
    "200 uA current source calibration I_cal = "
    f"{(labj.get_cal_current_source('200u') * 1e6):.3f} A"
)
print(
    "10 uA current source calibration I_cal = "
    f"{(labj.get_cal_current_source('10u') * 1e6):.3f} A"
)

print(f"State FIO0: {labj.get_digital_input('FIO0')}")

# configure and send pulse sequence.
labj.set_clock(clock_period=10)
labj.config_high_pulse(address="FIO3", t_start=0.5, t_width=1)
labj.config_high_pulse(address="FIO2", t_start=1, t_width=0.5)
labj.send_pulses("FIO3", "FIO2")
sleep(2)
labj.disable_pulses()


# stop device
labj.stop()
