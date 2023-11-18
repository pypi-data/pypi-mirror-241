#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script to demonstrate the capabilities of the a SST Luminox Oxygen sensor
device controller.
"""

import logging

from hvl_ccb.dev.sst_luminox import (
    Luminox,
    LuminoxMeasurementType,
    LuminoxOutputMode,
    LuminoxOutputModeError,
)

logging.basicConfig(level=logging.INFO)

# create device object
lumi = Luminox({"port": "COM5"})

# start the device
lumi.start()

# activate stream mode
lumi.activate_output(LuminoxOutputMode.polling)

print(f"percent o2: {lumi.query_polling(LuminoxMeasurementType.percent_o2)} %")
print(f'str1: percent o2: {lumi.query_polling("%")} %')
print(f'str2: percent o2: {lumi.query_polling("percent_o2")} %')
print(
    "barometric pressure: "
    f"{lumi.query_polling(LuminoxMeasurementType.barometric_pressure)} mbar"
)
print(
    "temperature sensor: "
    f"{lumi.query_polling(LuminoxMeasurementType.temperature_sensor)} °C"
)
print(
    "partial pressure o2: "
    f"{lumi.query_polling(LuminoxMeasurementType.partial_pressure_o2)} mbar"
)

print(
    "date of manufacture: "
    f"{lumi.query_polling(LuminoxMeasurementType.date_of_manufacture)}"
)
print(f"serial number: {lumi.query_polling(LuminoxMeasurementType.serial_number)}")
print(f"sensor status: {lumi.query_polling(LuminoxMeasurementType.sensor_status)}")
print(
    f"software revision: {lumi.query_polling(LuminoxMeasurementType.software_revision)}"
)

lumi.activate_output(LuminoxOutputMode.streaming)
print(lumi.read_streaming())

try:
    lumi.activate_output(LuminoxOutputMode.polling)
    lumi.read_streaming()
except LuminoxOutputModeError:
    pass
