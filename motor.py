import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
control_pins = [7,11,13,15]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

def open():
  halfsteps = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
  ]
  for i in range(100):
    for halfstep in range(8):
      for pin in range(4):
        GPIO.output(control_pins[pin], halfsteps[halfstep][pin])
      time.sleep(0.001)

def close():
  halfsteps = [
    [1,0,0,1],
    [0,0,0,1],
    [0,0,1,1],
    [0,0,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [1,1,0,0],
    [1,0,0,0]
  ]
  for i in range(100):
    for halfstep in range(8):
      for pin in range(4):
        GPIO.output(control_pins[pin], halfsteps[halfstep][pin])
      time.sleep(0.001)

open()
time.sleep(2)
close()
GPIO.cleanup()
