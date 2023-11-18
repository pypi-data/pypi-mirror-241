#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script for the device Pfeiffer TPG
"""

import logging

from hvl_ccb.dev.pfeiffer_tpg import PfeifferTPG

logging.basicConfig(level=logging.INFO)

# create device object
pg = PfeifferTPG({"port": "COM4"})

# start the device
pg.start()

# get the full scale range of all channels
# see model-dependent lookup table with: help(pg.get_full_scale)
fsr = pg.get_full_scale_mbar()

# set the full scale of sensor 5 to 100 mbar
fsr[4] = 100
pg.set_full_scale_mbar(fsr)

# get pressure reading from channel 1
pressure = pg.measure(1)

# get pressure reading from all channels
# (not available on all TPG models)
pressures = pg.measure_all()

# stop the device
pg.stop()
