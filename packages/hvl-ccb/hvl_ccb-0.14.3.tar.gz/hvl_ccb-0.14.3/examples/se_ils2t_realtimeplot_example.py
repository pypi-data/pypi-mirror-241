#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script for the device Schneider Electric ILS2T stepper motor. The script also
plots the position of the motor in real time (however, not as perfect, as desired;
this is considered as an alpha-state example).
"""

import logging

import matplotlib

matplotlib.use("TkAgg")
from time import sleep

import matplotlib.animation as animation
import matplotlib.pyplot as plt

from hvl_ccb.comm.modbus_tcp import ModbusTcpCommunication
from hvl_ccb.dev.se_ils2t import ILS2T

logging.basicConfig(level=logging.INFO)

# configuration dict with appropriate settings
com_config = {
    "host": "192.168.1.51",
    "unit": 255,
}

# create communication protocol object
com_device = ModbusTcpCommunication(com_config)

# create device object
ils2t = ILS2T(com_device)

# start the device
ils2t.start()

# Plotting
x_len = 500
y_range = [-160_000, 160_000]

# Create figure
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, x_len))
ys = [0] * x_len
ax.set_ylim(y_range)

(line,) = ax.plot(xs, ys, animated=True)

plt.title("SE ILS2T Position over Time")
plt.xlabel("Samples")
plt.ylabel("Position [steps]")


# animation function called on every update
def animate(i, ys):
    position = ils2t.get_position()

    ys.append(position)

    ys = ys[-x_len:]

    line.set_ydata(ys)

    return (line,)


ani = animation.FuncAnimation(fig, animate, fargs=(ys,), interval=100, blit=True)

plt.show()

ils2t.execute_relative_step(10 * 16_000)

print(f"Position: {ils2t.get_position()}")
print(f"Temperature: {ils2t.get_temperature()} °C")
print(f"DC Voltage: {ils2t.get_dc_volt()} V")
print(f"Status: {ils2t.get_status()}")

sleep(2)

ils2t.execute_relative_step(-10 * 16_000)
print(f"Position: {ils2t.get_position()}")
