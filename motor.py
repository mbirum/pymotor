import RPi.GPIO as GPIO
import time
import steps

GPIO.setmode(GPIO.BOARD)

control_pins = [7,11,13,15]
sleep = 0.001
mode = "full"

# initialize pins
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
  
def drive(step_sequence):
  for i in range(100):
    for step in range(len(step_sequence)):
      for pin in range(4):
        GPIO.output(control_pins[pin], step_sequence[step][pin])
      time.sleep(sleep)

def open():
  step_sequence = steps.getOpenHalf()
  if "full" == mode:
    step_sequence = steps.getOpenFull()
  drive(step_sequence)

def close():
  step_sequence = steps.getCloseHalf()
  if "full" == mode:
    step_sequence = steps.getCloseFull()
  drive(step_sequence)


open()
time.sleep(2)
close()

GPIO.cleanup()
