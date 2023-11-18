#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script demonstrating the R&S RTO 1024 oscilloscope
"""

import logging

from hvl_ccb.dev.rs_rto1024 import RTO1024, RTO1024Config

logging.basicConfig(level=logging.INFO)

dev_config = RTO1024Config(
    waveforms_path="C:\\Data\\DavidGraber\\02_waveforms",
    settings_path="C:\\Data\\DavidGraber\\01_settings",
    backup_path="D:\\backups",
)

rto = RTO1024({"host": "192.168.1.60"}, dev_config)

rto.start()
rto.get_channel_position(1)


print(rto.get_identification())
