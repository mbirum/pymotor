import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
control_pins = [7,11,13,15]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
forward = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

reverse = [
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
      GPIO.output(control_pins[pin], forward[halfstep][pin])
    time.sleep(0.001)
    
for i in range(100):
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins[pin], reverse[halfstep][pin])
    time.sleep(0.001)

GPIO.cleanup()
