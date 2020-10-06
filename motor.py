import RPi.GPIO as GPIO
import time
import steps
import sys

GPIO.setmode(GPIO.BOARD)

left_pins = [7,11,13,15]
right_pins = [16,18,22,32]
sleep = 0.001

# get mode as left or right
mode = sys.argv[1]

# assume left
control_pins = left_pins
open_sequence = steps.getForwardSequence()
close_sequence = steps.getBackwardSequence()

if "right" == mode:
  control_pins = right_pins
  open_sequence = steps.getBackwardSequence()
  close_sequence = steps.getForwardSequence()

"""
64  = 45 degrees
128 = 90 degrees
192 = 135 degrees
256 = 180 degrees
320 = 225 degrees
384 = 270 degrees
448 = 315 degrees
512 = 360 degrees
"""
rotation = ((128 - 64) / 2) + 64

# initialize pins
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
  
def drive(step_sequence):
  for i in range(rotation):
    for step in range(len(step_sequence)):
      for pin in range(4):
        GPIO.output(control_pins[pin], step_sequence[step][pin])
      time.sleep(sleep)

def open():
  drive(open_sequence)

def close():
  drive(close_sequence)

open()
time.sleep(2)
close()
GPIO.cleanup()