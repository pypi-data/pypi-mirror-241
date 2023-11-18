#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example Script how to work with the ExperimentManager using a LabJack device.
"""

import logging
import sys
from time import sleep

from apscheduler.schedulers.background import BackgroundScheduler

from hvl_ccb import ExperimentManager
from hvl_ccb.dev.labjack import LabJack

# configure logger
logging.basicConfig(level=logging.INFO)

# create background scheduler
scheduler = BackgroundScheduler()

# generate configuration dict
config = {
    "device_type": "T7",
    "connection_type": "ETHERNET",
    "identifier": "192.168.1.21",
}

# create device (using default communication protocol)
labj = LabJack(config)

# initialize experiment manager
mgr = ExperimentManager({"labj": labj})

# start ExperimentManager
mgr.run()


def print_temp_and_rh():
    print("Temp =", labj.get_sbus_temp(0) - 273.15, ", RH = ", labj.get_sbus_rh(0))


logging.getLogger("apscheduler").setLevel(logging.WARNING)
# scheduler.start()
scheduler.add_job(print_temp_and_rh, "interval", seconds=0.5)

try:
    while True:
        sleep(5)
        print("sleeping main thread...")
except (KeyboardInterrupt, SystemExit):
    print("Interrupt caught")
    scheduler.shutdown()
    mgr.finish()
    sys.exit(0)
