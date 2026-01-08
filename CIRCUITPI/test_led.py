import time
import board
from digitalio import DigitalInOut, Direction
                                                              # specify hardware
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
                                                                # toggle the LED
while True:
    led.value = False
    time.sleep(0.5)
    led.value = True
    time.sleep(0.5)
