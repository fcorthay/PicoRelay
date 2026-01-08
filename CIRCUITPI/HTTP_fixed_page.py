import os
import socketpool
import wifi
from adafruit_httpserver import Request, Response, Server
                                                                     # constants
SERVER_PORT = 80
HTML_PAGE = """
<html lang="en">
    <head>
        <title>Hello from RPi Pico</title>
    </head>
    <body>
        <p>
            Hello from RPi Pico
        </p>
    </body>
</html>
"""
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
                                                     # define a route to respond
@server.route("/")
def base(request: Request):
    """
    Serve a default static plain text message.
    """
    return Response(request, HTML_PAGE, content_type="text/html")
                                                                # run the server
server.serve_forever(str(wifi.radio.ipv4_address), port=SERVER_PORT)
