import os
import socketpool
import wifi
from adafruit_httpserver import Request, Response, Server
                                                                     # constants
SERVER_PORT = 80
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
server = Server(pool, "/static", debug=True)
                                                     # define a route to respond
@server.route("/")
def base(request: Request):
    """
    Serve a default static plain text message.
    """
    return Response(request, "Hello from the CircuitPython HTTP Server!")
                                                                # run the server
server.serve_forever(str(wifi.radio.ipv4_address), port=SERVER_PORT)
