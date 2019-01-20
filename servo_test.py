#!/usr/bin/python3
"""
Pymata-aio port of the Arduino Servo --> Sweep Example
"""
from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import sys
import signal

board = PyMata3()

step = 2
gap = 0.025

SERVO_PIN_A = 9     # left motor controller 
SERVO_PIN_B = 10    # right motor controller
SERVO_PIN_C = 11    # servo


def setup():
    board.servo_config(SERVO_PIN_A)
    board.servo_config(SERVO_PIN_B)
    board.servo_config(SERVO_PIN_C)

def calibrate():
        board.analog_write(SERVO_PIN_A, 90)
        board.analog_write(SERVO_PIN_B, 90)
        board.analog_write(SERVO_PIN_C, 90)
        #sleep(1000)
        board.analog_write(SERVO_PIN_A, 0)
        board.analog_write(SERVO_PIN_B, 0)
        board.analog_write(SERVO_PIN_C, 0)
        #sleep(1000)
        board.analog_write(SERVO_PIN_A, 90)
        board.analog_write(SERVO_PIN_B, 90)
        board.analog_write(SERVO_PIN_C, 90)
        #sleep(1000)
        board.analog_write(SERVO_PIN_A, 180)
        board.analog_write(SERVO_PIN_B, 180)
        board.analog_write(SERVO_PIN_C, 180)
        #sleep(1000)
        board.analog_write(SERVO_PIN_A, 90)
        board.analog_write(SERVO_PIN_B, 90)
        board.analog_write(SERVO_PIN_C, 90)
        #sleep(1000)

def loop():
    print("Servo up")
    # The range of motion for some servos isn't all the way from 0 degrees to 180 degrees, change as needed.
    for pos in range(0, 180,step): # Start=0 degrees, Finish=180 degree, (Increment=1 degree which is the default)
        print(str(pos))
        board.analog_write(SERVO_PIN_A, pos)
        board.analog_write(SERVO_PIN_B, pos)
        board.analog_write(SERVO_PIN_C, pos)
        board.sleep(gap)
    print("Servo down")
    for pos in range(180, 0, -step): # Start=180 degrees, Finish=0 degrees, Increment=-1 degrees (moving down)
        print(str(pos))
        board.analog_write(SERVO_PIN_A, pos)
        board.analog_write(SERVO_PIN_B, pos)
        board.analog_write(SERVO_PIN_C, pos)
        board.sleep(gap)


if __name__ == "__main__":
    setup()
    calibrate()
    while True:
        loop()


