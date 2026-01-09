import os
import board
from digitalio import DigitalInOut, Direction
import socketpool
import wifi
from adafruit_httpserver import Request, Response, Server
                                                                     # constants
SERVER_PORT = 80
HOME_PAGE = """
<html lang="en">
 <head>
  <title>RPi Pico relay control</title>
 </head>
 <body>
  <p>
   This web service allows to control a
   <a href="https://github.com/fcorthay/PicoRelay">PicoRelay</a>
   board.
  </p>
  <p>
   Check the relay statuses in the <a href="/relays">status</a> page.
  </p>
 </body>
</html>
"""
STATUS_PAGE = """
<html lang="en">
 <head>
  <title>RPi Pico relay control</title>
 </head>
 <body>
  <p>
   relay 1 is relay1_value
   <br />
   relay 2 is relay2_value
  </p>
 </body>
</html>
"""
RELAY_VALUE_PAGE = """
<html lang="en">
 <head>
  <title>RPi Pico relay control</title>
 </head>
 <body>
  <p>
   relay relay_id is relay_state
  </p>
 </body>
</html>
"""
RELAY_SET_PAGE = """
<html lang="en">
 <head>
  <title>RPi Pico relay control</title>
 </head>
 <body>
  <p>
   relay relay_id set to relay_state
  </p>
 </body>
</html>
"""
INDENT = 2*' '
                                                              # specify hardware
relay1 = DigitalInOut(board.GP6)
relay1.direction = Direction.OUTPUT
relay2 = DigitalInOut(board.GP7)
relay2.direction = Direction.OUTPUT

# ------------------------------------------------------------------------------
# functions
# ------------------------------------------------------------------------------
                                                               # get relay value
def get_relay_state(relay_id) :
    boolean_value = relay1.value
    if relay_id == 2 :
        boolean_value = relay2.value

    if boolean_value :
        value = 'on'
    else :
        value = 'off'

    return(value)
                                                               # set relay value
def set_relay(relay_id, state) :
    value = True
    if state == 'off' :
        value = False
    print("setting relay %d to %s" % (relay_id, state))

    if relay_id == 1 :
        relay1.value = value
    elif relay_id == 2 :
        relay2.value = value

# ------------------------------------------------------------------------------
                                                             # Wi-Fi credentials
wifi_ssid = os.getenv('CIRCUITPY_WIFI_SSID')
wifi_password = os.getenv('CIRCUITPY_WIFI_PASSWORD')
                                                              # connect to Wi-Fi
print()
print("Connecting to \"%s\" Wi-Fi" % wifi_ssid)
wifi.radio.connect(wifi_ssid, wifi_password)
print(INDENT + 'Connected')
IP_address = str(wifi.radio.ipv4_address)
                                                           # create a web server
pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, debug=True)
                                                                     # home page
@server.route("/")
def serve_home_page(request: Request) :
    return Response(request, HOME_PAGE, content_type="text/html")
                                                                   # status page
@server.route("/relays")
def serve_home_page(request: Request) :
    relay1_value = get_relay_value(1)
    relay2_value = get_relay_value(2)
    html_page = STATUS_PAGE
    html_page = html_page.replace('relay1_value', relay1_value)
    html_page = html_page.replace('relay2_value', relay2_value)
    return Response(request, html_page, content_type="text/html")
                                                             # read relay status
@server.route("/relay/<relay_id>")
def show_relay_state(request: Request, relay_id: str) :
    relay_state = get_relay_state(int(relay_id))
    html_page = RELAY_VALUE_PAGE
    html_page = html_page.replace('relay_id', relay_id)
    html_page = html_page.replace('relay_state', relay_state)
    return Response(request, html_page, content_type="text/html")
                                                                     # act relay
@server.route("/relay/<relay_id>/<relay_state>")
def act_relay(request: Request, relay_id: str, relay_state: str) :
    if (relay_state == '0') :
        relay_state = 'off'
    if (relay_state == '1') :
        relay_state = 'on'
    set_relay(int(relay_id), relay_state)
    html_page = RELAY_SET_PAGE
    html_page = html_page.replace('relay_id', relay_id)
    html_page = html_page.replace('relay_state', relay_state)
    return Response(request, html_page, content_type="text/html")
                                                                # run the server
server.serve_forever(IP_address, port=SERVER_PORT)
