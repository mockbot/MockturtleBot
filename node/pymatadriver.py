#!/usr/bin/python3

VERSION="2018-12-29"

print("PymataDriver "+VERSION+"\n")

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import sys
import signal

# callback for adc input, e.g. battery voltage
def adc_callback(data):
    # data[0] is the pin number and data[1] is the changed value
    print("ADC"+str(data[0])+":"+str(data[1]))
    #return (data[0],data[1])

try:
    board = PyMata3()
    board.set_pin_mode(0, Constants.ANALOG, adc_callback)
    board.set_pin_mode(1, Constants.ANALOG, adc_callback)
    '''
    board.set_pin_mode(2, Constants.ANALOG, adc_callback)
    board.set_pin_mode(3, Constants.ANALOG, adc_callback)
    board.set_pin_mode(4, Constants.ANALOG, adc_callback)
    board.set_pin_mode(5, Constants.ANALOG, adc_callback)
    board.set_pin_mode(6, Constants.ANALOG, adc_callback)
    board.set_pin_mode(7, Constants.ANALOG, adc_callback)
    '''

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
