#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#

import logging
from time import sleep

import hvl_ccb.dev.highland_t560 as highland

logging.basicConfig(level=logging.DEBUG)

com = {"host": "172.31.56.60", "port": 9999}

# Create and start device:
dg = highland.T560(com)
dg.start()
# Ensure configuration settings will be installed immediately:
dg.auto_install_mode = 1
# Load most recently saved settings:
dg.load_device_configuration()
# Ensure all trigger modes are off for device configuration:
dg.disarm_trigger()
# Prepare pulses to be sent on channels A&B:
dg.ch_a.enabled = True
dg.ch_b.enabled = True
dg.ch_a.polarity = "POS"
dg.ch_b.polarity = "POS"
dg.ch_a.delay = 0
dg.ch_a.width = 1e-9
dg.ch_b.delay = 5e-6
dg.ch_b.width = 1e-4
dg.trigger_mode = highland.TriggerMode.COMMAND
# Send pulses twice:
dg.fire_trigger()
sleep(0.5)
dg.fire_trigger()
# Switch to internal triggering
dg.frequency = 10_000_000
dg.trigger_mode = highland.TriggerMode.INT_SYNTHESIZER
sleep(0.1)
dg.disarm_trigger()
# Add a channel and arm external trigger, using trigger gating
dg.ch_c.enabled = True
dg.ch_c.polarity = "POS"
dg.gate_mode = highland.GateMode.INPUT
dg.ch_c.delay = 5e-3
dg.ch_c.width = 1e-6
dg.trigger_mode = highland.TriggerMode.EXT_RISING_EDGE
# Save these settings and close the device
dg.save_device_configuration()
dg.stop()
