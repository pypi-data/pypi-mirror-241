#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script for a Technix capacitor charger with a telnet connection
"""
import logging
from time import sleep

import hvl_ccb.dev.technix as technix

logging.basicConfig(level=logging.INFO)


#: Configuration of the connection
com = {"host": "charger.lan"}
#: Configuration of the device, here also the type of the connection is chosen
dev_config = {
    "max_voltage": 10000,
    "max_current": 1.5,
    "communication_channel": technix.TechnixTelnetCommunication,
}

#: Initialise
tex = technix.Technix(com, dev_config)

#: Start connection (also starts the polling of the status)
tex.start()
tex.query_status()

print(f"Interlock: {tex.open_interlock}")

while tex.open_interlock:
    print("Cannot operate without allowance from safety circuit.")
    sleep(5)

tex.voltage = 100
tex.current = 0.01

tex.output = True
sleep(1)  # The device needs some time to start charging
tex.query_status()
while tex.current >= 0.001:
    print(f"Voltage: {tex.voltage:.0f} V")
    print(f"Current: {tex.current:.3f} A")
    sleep(0.5)

print(f"Finished charging up to {tex.voltage:.0f} V")

# Inhibit the output
tex.inhibit = True
sleep(2)

tex.voltage = 150

tex.inhibit = False
sleep(1)
# Continue charging
tex.query_status()
while tex.current >= 0.001:
    print(f"Voltage: {tex.voltage:.0f} V")
    print(f"Current: {tex.current:.3f} A")
    sleep(0.5)

print(f"Finished charging up to {tex.voltage:.0f} V")

tex.output = False
tex.stop()

print("Finished charging!")
