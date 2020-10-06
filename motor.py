import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
control_pins = [7,11,13,15]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

#for i in range(512):
#  for halfstep in range(8):
#    for pin in range(4):
#      GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
#    time.sleep(0.001)

delay = 0.001

setStep(1, 0, 1, 0)
time.sleep(delay)
setStep(0, 1, 1, 0)
time.sleep(delay)
setStep(0, 1, 0, 1)
time.sleep(delay)
setStep(1, 0, 0, 1)
time.sleep(delay)

GPIO.cleanup()

def setStep(w1, w2, w3, w4):
  control_pins[0].value = w1
  control_pins[1].value = w2
  control_pins[2].value = w3
  control_pins[3].value = w4


