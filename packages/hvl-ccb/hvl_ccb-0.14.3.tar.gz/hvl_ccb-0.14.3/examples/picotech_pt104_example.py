#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
This example shows how to use the Pico Technologies PT104 data logger to read the
temperature from a 4-wire pt100 sensor on channel 1.

To use a PT-104 device wrapper:

1. install the `hvl_ccb` package with a `picotech` extra feature::

        $ pip install "hvl_ccb[picotech]"

   this will install the Python bindings for the library.

2. install the additional system library

    * on Windows: download and install PicoSDK from https://www.picotech.com/downloads
      (choose "PicoLog Data Loggers" > "PT-104" > "Software");
    * on Linux:
        - for Ubuntu/Debian, install `libusbpt104` from `.deb` file found in
          https://labs.picotech.com/debian/pool/main/libu/libusbpt104/ (note: at the
          moment the PT-104 driver is not a part of the official `picoscope`
          package; cf.
          https://www.picotech.com/support/topic40626.html );
        - for any other supported Linux distribution, follow instructions to install
          the "USB PT-104 devices" drivers in https://www.picotech.com/downloads/linux ;
"""

import logging
import time

from hvl_ccb.dev.picotech_pt104 import picotech_pt104 as pt

# Configure logger
logging.basicConfig(level=logging.INFO)

# Specify ip, serial number and communication mode of PT104 device
config = {
    "host": "192.168.0.4",
    "port": 6249,
    "serial_number": "HS337/135",
    "interface": pt.Pt104CommunicationType.ETHERNET,
}

# Open device
pico = pt.Pt104({}, config)

# Start device
pico.start()
time.sleep(1)

# Configure channel 2 to read data from a 4-wire pt100 sensor with low-pass filter off
pico.set_channel(
    pt.Pt104Channels.CHANNEL_2, pt.Pt104DataTypes.PT100, pt.Pt104Wires.WIRES_4, False
)
time.sleep(1)

# Read and print the temperature from channel 1 once a second for 5 seconds
for n in range(5):
    print("Temperature read on channel 1: ", pico.get_value_channel_2)
    time.sleep(1)


# Close device
pico.stop()
