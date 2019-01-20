#!/usr/bin/python3

VERSION="2018-12-29"

print("Pymata Sonar Ping Test "+VERSION+"\n")

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import sys
import signal


# ping callback function
def cb_ping(data):
    if data[1] > 0:
        sonar_distance=data[1]/100
        print(str(sonar_distance) + ' m')


try:
    board = PyMata3()
    board.sonar_config(12, 12, cb_ping)

except KeyboardInterrupt:
    sys.exit(0)


# Signal handler to trap control C
def _signal_handler(sig, frame):
    if board is not None:
        print('\nYou pressed Ctrl+C')
        sys.exit(1)


signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)

# add SIGALRM if platform is not windows
if not sys.platform.startswith('win32'):
    signal.signal(signal.SIGALRM, _signal_handler)

while True:
    board.sleep(.1)
