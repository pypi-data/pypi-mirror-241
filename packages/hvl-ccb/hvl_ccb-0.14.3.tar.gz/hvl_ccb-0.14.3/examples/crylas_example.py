#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script for the devices CryLasLaser and CrylasAttenuator
"""

import logging

from hvl_ccb import ExperimentManager
from hvl_ccb.dev.crylas import CryLasAttenuator, CryLasLaser, CryLasLaserConfig

logging.basicConfig(level=logging.INFO)

# create devices with configuration
crylas = ExperimentManager({
    "las": CryLasLaser(
        {"port": "COM10"},
        {
            "auto_laser_on": True,
            "init_shutter_status": CryLasLaserConfig.ShutterStatus.CLOSED,
        },
    ),
    "att": CryLasAttenuator({"port": "COM12"}, {"init_attenuation": 0}),
})
print(crylas.status)

# start the laser (will also turn on the laser if 'auto_laser_on' is True, and set the
# shutter in the configured position, ex: CryLasLaserConfig.ShutterStatus.CLOSED)
crylas.start()
print(crylas.status)

# change the repetition rate (internal software trigger): 10, 20 or 60 Hz
crylas.las.set_repetition_rate(10)

# open the shutter
crylas.las.open_shutter()

# wait until the laser is on (this can take up to 5 minutes)
crylas.las.wait_until_ready()

# change the percentage of transmitted light (same as las.set_attenuation(20))
crylas.att.set_transmission(80)

# get the current pulse energy and rate
# rate = 0, means using internal hardware trigger
energy, rate = crylas.las.get_pulse_energy_and_rate()
print(f"Energy: {energy} uJ, rate: {rate} Hz")

# turn off the laser
crylas.las.laser_off()

# ... do stuff

# turn the laser on again
crylas.las.laser_on()

# set the pulse energy in uJ (possible only when using an external hardware trigger)
crylas.las.set_pulse_energy(100)

# stop the laser controller (this turns off the laser and closes the shutter) and the
# attenuator
crylas.stop()
print(crylas.status)
