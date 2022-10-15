import rp2
import network
import ubinascii
import machine
import urequests as requests
import time
import socket
from secrets import secrets
from machine import Pin
from PiicoDev_Unified import sleep_ms

# Set country to avoid possible errors
rp2.country('AU')

# ssid = 'SteebAndroidAP'
# password = 'tndz1729'

ssid = 'TelstraE7B5FF'
password = 'k5t37y9ucj'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print(mac)

# power saving mode off:
# wlan.config(pm = 0xa11140)

wlan.connect(ssid, password)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
    
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('Connected to Telstra WiFi')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

# Connection Status Codes
#define CYW43_LINK_DOWN (0)
#define CYW43_LINK_JOIN (1)
#define CYW43_LINK_NOIP (2)
#define CYW43_LINK_UP (3)
#define CYW43_LINK_FAIL (-1)
#define CYW43_LINK_NONET (-2)
#define CYW43_LINK_BADAUTH (-3)




# Broadcast the access point of this Pico W
essid = 'Pico-W-Weather-Station'
password = '#FreeThePicoW'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=essid, password=password)

while ap.active() == False:
    pass

print('Broadcasting Access Point')
print(ap.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(3)
#blink_onboard_led(3, 0.2)





# Start up the SSD OLED display
from PiicoDev_SSD1306 import PiicoDev_SSD1306

import math
from PiicoDev_SSD1306 import *

display = create_PiicoDev_SSD1306()

# Text and numbers
for counter in range(0,101):
    display.fill(0)
    display.text("PiicoDev",30,20, 1)
    display.text(str(counter),50,35, 1)
    display.show()
sleep_ms(500)

# Bargraphs
thick = 15 # thickness of the bar
for val in range(WIDTH+1):
    display.fill(0)
    display.text("Bargraphs", 20, 10, 1)
    display.fill_rect(0, HEIGHT-thick, val, thick, 1) # Filled bar graph
    display.rect(0, int(HEIGHT-2*thick - 5), int(val/2), thick, 1) # no-fill
    display.show()
sleep_ms(500)

# Plots
graphSin = display.graph2D()
graphCos = display.graph2D()
for x in range(128):
    s = int(math.sin(x/10.0)*HEIGHT+HEIGHT+30)
    c = int(math.cos(x/10.0)*HEIGHT+HEIGHT+30)
    display.fill(0)
    display.text("Plots", 50, 10, 1)
    display.updateGraph2D(graphSin,s)
    display.updateGraph2D(graphCos,c)
    display.show()
sleep_ms(3000)

# Display a portable bitmap image (.pbm)
from PiicoDev_SSD1306 import *
display = create_PiicoDev_SSD1306()
display.fill(0)
display.load_pbm('bone.pbm', 1)
display.show()
sleep_ms(5000)

# Begin READING atmospheric information
from PiicoDev_BME280 import PiicoDev_BME280

sensor = PiicoDev_BME280() # initialise the sensor
zeroAlt = sensor.altitude() # take an initial altitude reading
print('Temperature, air pressure, and humidty readings')
while True:
    # Print data
    tempC, presPa, humRH = sensor.values() # read all data from the sensor
    pres_hPa = presPa / 100 # convert air pressurr Pascals -> hPa (or mbar, if you prefer)
    print(str(tempC)+"°C " + str(pres_hPa)+"hPa " + str(humRH)+"% humidity")
    
    # Altitude demo
    print(sensor.altitude() - zeroAlt) # Print the pressure CHANGE since the script began
    sleep_ms(3000)


