import os
import wifi
                                                             # Wi-Fi credentials
wifi_ssid = os.getenv('CIRCUITPY_WIFI_SSID')
wifi_password = os.getenv('CIRCUITPY_WIFI_PASSWORD')
                                                              # connect to Wi-Fi
print()
print("Connecting to \"%s\" Wi-Fi" % wifi_ssid)
wifi.radio.connect(wifi_ssid, wifi_password)
                                                                  # show address
print("The RPi's IP address is %s" % wifi.radio.ipv4_address)
