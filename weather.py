import pyowm
import unicornhat as uh
import time
import sys
from modules import owmapikey

id = int(input('City ID: '))
#for arg in sys.argv[1:]:
#	print arg

uh.set_layout(uh.PHAT)
uh.brightness(0.7)

owm = pyowm.OWM(owmapikey.strApiKey)
w = owm.weather_at_id(id)
wd = w.get_weather()
tempF = wd.get_temperature('fahrenheit')['temp']
print tempF

if tempF < 60.0:
        a = 0  
        b = 0
        c = 255
elif tempF < 70.0:
	a = 0
	b = 255
	c = 0
#elif tempF < 80.0:
else:
	a = 255
	b = 0
	c = 0

for x in range(8):
        for y in range(4):
                uh.set_pixel(x, y, a, b, c)
uh.show()
time.sleep(5)
