import os
import board
from digitalio import DigitalInOut, Direction
import socketpool
import wifi
from adafruit_httpserver import Request, Response, Server
                                                                     # constants
PIN_NB = 23
SERVER_PORT = 80
HTML_PAGE = """
<html lang="en">
    <head>
        <title>RPi Pico pin control</title>
    </head>
    <body>
        <p>
            Pin pin_id is pin_value
        </p>
    </body>
</html>
"""
                                                                      # pin list
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
                                                             # Wi-Fi credentials
wifi_ssid = os.getenv('CIRCUITPY_WIFI_SSID')
wifi_password = os.getenv('CIRCUITPY_WIFI_PASSWORD')
                                                              # connect to Wi-Fi
print()
print("Connecting to \"%s\" Wi-Fi" % wifi_ssid)
wifi.radio.connect(wifi_ssid, wifi_password)
print("Connected to %s" % wifi_ssid)
                                                           # create a web server
pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, debug=True)
                                                                # read pin value
@server.route("/pin/<pin_id>")
def get_pin_value(request: Request, pin_id: str):
    pin_value = pins[int(pin_id)].value
    if pin_value :
        pin_value_print = 'high'
    else :
        pin_value_print = 'low'
    html_page = HTML_PAGE
    html_page = html_page.replace('pin_id', pin_id)
    html_page = html_page.replace('pin_value', pin_value_print)
    return Response(request, html_page, content_type="text/html")
                                                               # write pin value
@server.route("/pin/<pin_id>/<pin_value>")
def get_pin_value(request: Request, pin_id: str, pin_value: str):
    new_value = False
    if (pin_value == '1') or (pin_value == 'high') or (pin_value == 'true') :
        new_value = True
    pin = pins[int(pin_id)]
    pin.direction = Direction.OUTPUT
    pin.value = new_value
    if new_value :
        pin_value_print = 'high'
    else :
        pin_value_print = 'low'
    html_page = HTML_PAGE
    html_page = html_page.replace('pin_id', pin_id)
    html_page = html_page.replace('pin_value', pin_value_print)
    html_page = html_page.replace(' is ', ' set to ')
    return Response(request, html_page, content_type="text/html")
                                                                # run the server
server.serve_forever(str(wifi.radio.ipv4_address), port=SERVER_PORT)
