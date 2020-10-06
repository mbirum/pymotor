import RPi.GPIO as GPIO
import time
import steps

GPIO.setmode(GPIO.BOARD)

left_pins = [7,11,13,15]
right_pins = [16,18,22,32]
sleep = 0.001

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
#rotation = ((128 - 64) / 2) + 64
rotation = 3

# initialize pins
for pin in left_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

for pin in right_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
  
def drive(step_sequence):
  for i in range(rotation):
    for step in range(len(step_sequence)):
      for pin in range(4):
        GPIO.output(right_pins[pin], step_sequence[step][pin])
      time.sleep(sleep)

def open():
  drive(steps.getOpenSequence())

def close():
  drive(steps.getCloseSequence())

#open()
time.sleep(2)
close()
GPIO.cleanup()