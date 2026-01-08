import time
import board
from digitalio import DigitalInOut, Direction
                                                              # specify hardware
relay1 = DigitalInOut(board.GP6)
relay1.direction = Direction.OUTPUT
relay2 = DigitalInOut(board.GP7)
relay2.direction = Direction.OUTPUT
                                                           # toggle the switches
for index in range(10) :
    print(index)
    relay1.value = False
    time.sleep(0.5)
    relay2.value = True
    time.sleep(0.5)
    relay1.value = True
    time.sleep(0.5)
    relay2.value = False
    time.sleep(0.5)
