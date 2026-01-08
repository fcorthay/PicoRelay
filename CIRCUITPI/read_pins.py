import time
import board
from digitalio import DigitalInOut, Direction
                                                                     # constants
PIN_NB = 23
PIN_NB = 10
                                                              # specify hardware
pin0 = DigitalInOut(board.GP0)
pin1 = DigitalInOut(board.GP1)
pin2 = DigitalInOut(board.GP2)
pin3 = DigitalInOut(board.GP3)
pin4 = DigitalInOut(board.GP4)
pin5 = DigitalInOut(board.GP5)
pin6 = DigitalInOut(board.GP6)
pin7 = DigitalInOut(board.GP7)
pin8 = DigitalInOut(board.GP8)
pin9 = DigitalInOut(board.GP9)
pin10 = DigitalInOut(board.GP10)
pin11 = DigitalInOut(board.GP11)
pin12 = DigitalInOut(board.GP12)
pin13 = DigitalInOut(board.GP13)
pin14 = DigitalInOut(board.GP14)
pin15 = DigitalInOut(board.GP15)
pin16 = DigitalInOut(board.GP16)
pin17 = DigitalInOut(board.GP17)
pin18 = DigitalInOut(board.GP18)
pin19 = DigitalInOut(board.GP19)
pin20 = DigitalInOut(board.GP20)
pin21 = DigitalInOut(board.GP21)
pin22 = DigitalInOut(board.GP22)
pins = []
for index in range(PIN_NB) :
 eval("pins.append(pin%d)" % index)
                                                            # display pin values
for index in range(len(pins)) :
    print(pins[index].value)
print()
                                                               # set a pin value
pin6.direction = Direction.OUTPUT
pin6.value = True
                                                            # display pin values
for index in range(len(pins)) :
    print(pins[index].value)
print()
                                                          # delay before exiting
time.sleep(10)
