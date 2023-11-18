#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script for using a LEM 4000 S sensor.
"""

import logging

from hvl_ccb.utils.conversion import LEM4000S, LMT70A

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)40s %(levelname)8s %(message)s",
)

lem = LEM4000S()
lem.calibration_factor = 1.01
lem.shunt = 1

lem.convert((0.12, 0.24, 0.138))
lem.convert(0.8)


lt = LMT70A()
lt.convert(0.65)
lt.convert([0.65, 0.75])
