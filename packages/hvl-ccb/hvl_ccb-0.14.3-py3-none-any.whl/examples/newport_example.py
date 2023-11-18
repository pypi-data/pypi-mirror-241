#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script for the device Newport SMC100PP
"""

import logging

from hvl_ccb.dev.newport import NewportSMC100PP, NewportSMC100PPConfig

logging.basicConfig(level=logging.INFO)

# create device object
mot_config = {
    "address": 1,
    "user_position_offset": 23.987,
    "screw_scaling": 1.00188172,
    "acceleration": 10,
    "backlash_compensation": 0,
    "hysteresis_compensation": 0.015,
    "micro_step_per_full_step_factor": 100,
    "motion_distance_per_full_step": 0.01,
    "home_search_type": NewportSMC100PPConfig.HomeSearch.HomeSwitch,
    "jerk_time": 0.04,
    "home_search_velocity": 4,
    "home_search_timeout": 27.5,
    "peak_output_current_limit": 0.4,
    "rs485_address": 2,
    "negative_software_limit": -24,
    "positive_software_limit": 26,
    "velocity": 4,
    "base_velocity": 0,
    "stage_configuration": NewportSMC100PPConfig.EspStageConfig.EnableEspStageCheck,
}
mot = NewportSMC100PP({"port": "COM5"}, mot_config)

# start() opens the com, and if the controller is in state NO_REF state:
# * applies the config
# * initialize the controller (put the motor to its home position and the controller in
# READY state)
mot.start()

# move the motor to a certain absolute positive
mot.move_to_absolute_position(40)
mot.wait_until_move_finished()

# move the motor relatively to the current position
mot.move_to_relative_position(-10)
mot.wait_until_move_finished()

# send the motor to its home position, which corresponds to 'user_position_offset'
mot.go_home()
mot.wait_until_move_finished()

# stop() ceases the motion of the motor and closes the com. Use mot.stop_motion() if you
# want only to cease the motion.
mot.stop()
