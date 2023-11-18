#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Example script for a telnet connection
"""
from hvl_ccb.comm.telnet import TelnetCommunication

config = {"host": "www.w3.org", "port": 80}
tc = TelnetCommunication(config)
tc.open()
tc.write("GET / HTTP/1.1")
tc.write(f"HOST: {config['host']}")
tc.write("")

answer = tc.read_all(attempt_interval_sec=0.1)

if len(answer) == 0:
    print("No answer")
elif len(answer) <= 150:
    print(answer)
else:
    print(answer[:150])
