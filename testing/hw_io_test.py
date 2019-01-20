#!/usr/bin/python3
'''
Arduino Pymata Firmata IO Test
'''

VERSION="2019-01-20-2220"

print("Pymata HW IO Test "+VERSION+"\n")

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import sys
import signal

SERVO_PIN_A = 9     # left motor controller
SERVO_PIN_B = 10    # right motor controller
SERVO_PIN_C = 11    # servo

# callback for adc input, e.g. battery voltage
def adc_callback(data):
    # data[0] is the pin number and data[1] is the changed value
    print("ADC"+str(data[0])+":"+str(data[1]))

# callback for ultra sonic sensor, e.g. distance to object
def ping_callback(data):
  if data[1] > 0:
    sonar_distance=data[1]/100
    print("USS"+str(data[0])+":"+str(sonar_distance))

# calibrate motorcontroller for position NULL=90
def calibrate_servos():
    board.analog_write(SERVO_PIN_A, 90)
    board.analog_write(SERVO_PIN_B, 90)
    board.analog_write(SERVO_PIN_C, 90)
    board.analog_write(SERVO_PIN_A, 0)
    board.analog_write(SERVO_PIN_B, 0)
    board.analog_write(SERVO_PIN_C, 0)
    board.analog_write(SERVO_PIN_A, 90)
    board.analog_write(SERVO_PIN_B, 90)
    board.analog_write(SERVO_PIN_C, 90)
    board.analog_write(SERVO_PIN_A, 180)
    board.analog_write(SERVO_PIN_B, 180)
    board.analog_write(SERVO_PIN_C, 180)
    board.analog_write(SERVO_PIN_A, 90)
    board.analog_write(SERVO_PIN_B, 90)
    board.analog_write(SERVO_PIN_C, 90)

def setup()
  # initialise arduino board
  board = PyMata3()
  # setup ADC pins
  board.set_pin_mode(0, Constants.ANALOG, adc_callback)
  board.set_pin_mode(1, Constants.ANALOG, adc_callback)
  board.set_pin_mode(2, Constants.ANALOG, adc_callback)
  board.set_pin_mode(3, Constants.ANALOG, adc_callback)
  board.set_pin_mode(4, Constants.ANALOG, adc_callback)
  board.set_pin_mode(5, Constants.ANALOG, adc_callback)
  board.set_pin_mode(6, Constants.ANALOG, adc_callback)
  board.set_pin_mode(7, Constants.ANALOG, adc_callback)
  # setup ultra sonar pin
  board.sonar_config(12, 12, ping_callback)
  # setup servo pins, e.g. motor controller or servos
  board.servo_config(SERVO_PIN_A)
  board.servo_config(SERVO_PIN_B)
  board.servo_config(SERVO_PIN_C)

# Signal handler to trap control C
def _signal_handler(sig, frame):
    if board is not None:
        print('\nCtrl+C for abort detected')
        sys.exit(1)

signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)

# add SIGALRM if platform is not windows
if not sys.platform.startswith('win32'):
    signal.signal(signal.SIGALRM, _signal_handler)

try:
  setup()
  calibrate_servos()
except KeyboardInterrupt:
    sys.exit(0)

while True:
    board.sleep(.1)
