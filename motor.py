import RPi.GPIO as GPIO
import time
import steps

GPIO.setmode(GPIO.BOARD)

control_pins = [7,11,13,15]
sleep = 0.001

# initialize pins
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
  
def drive(step_sequence):
  for i in range(64):
    for step in range(len(step_sequence)):
      for pin in range(4):
        GPIO.output(control_pins[pin], step_sequence[step][pin])
      time.sleep(sleep)

def open():
  drive(steps.getOpenSequence())

def close():
  drive(steps.getCloseSequence())

open()
#time.sleep(2)
#close()
GPIO.cleanup()