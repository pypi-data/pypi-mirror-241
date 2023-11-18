#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script for a Fluke8845a multimeter with telnet connection
usage measurement_function: "VOLT" or MeasurementFunction.VOLTAGE_DC both work
"""

import logging

from hvl_ccb.dev.fluke884x import (  # noqa: F401
    Fluke8845a,
    MeasurementFunction,
    TriggerSource,
)

logging.basicConfig(level=logging.DEBUG)

#: Configuration of the connection
com = {"host": "192.168.1.6", "wait_sec_read_text_nonempty": 1}

#: Initialise
tex = Fluke8845a(com)

#: Start connection (also starts the polling of the status)
tex.start()
# tex.identification
# tex.display_enable = True
# tex.display_message = "Hi123456321321222786"
# tex.clear_display_message()

"""
VOLTAGE MEASUREMENT
"""
# tex.measurement_function = "VOLT"
# tex.measurement_function = MeasurementFunction.VOLTAGE_DC
# tex.dc_voltage_range = 5
#
# tex.measurement_function = "VOLT:AC"
# tex.measurement_function = MeasurementFunction.VOLTAGE_AC
# tex.ac_voltage_range = 0.8


"""
CURRENT MEASUREMENT
"""
# tex.measurement_function = "CURR"
# tex.measurement_function = MeasurementFunction.CURRENT_DC
# tex.dc_current_range = 0.8

# tex.measurement_function = "CURR:AC"
# tex.measurement_function = MeasurementFunction.CURRENT_AC
# tex.ac_current_range = 0.8
# tex.current_filter = 20

"""
RESISTANCE MEASUREMENT
"""
# tex.measurement_function = "RES"
# # tex.measurement_function = MeasurementFunction.TWO_WIRE_RESISTANCE
# tex.two_wire_resistance_range = 2010

# tex.measurement_function = "FRES"
# # tex.measurement_function = MeasurementFunction.FOUR_WIRE_RESISTANCE
# tex.four_wire_resistance_range = 2010

"""
FREQUENCY AND PERIOD
"""
# tex.measurement_function = "FREQ"
# tex.measurement_function = MeasurementFunction.FREQUENCY
# tex.frequency_aperture = 0.1
#
# tex.measurement_function = "PER"
# tex.measurement_function = MeasurementFunction.PERIOD
# tex.period_aperture = 0.1

"""
TRIGGER
"""
# tex.trigger_source = "BUS"
tex.trigger_source = TriggerSource.BUS
tex.trigger_delay = 1

data = tex.measure()
tex.stop()
