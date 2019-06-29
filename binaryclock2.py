from division5 import findBinary
import unicornhat as uh
import time
from ledweather import weather

def selectLed(a):
	if a == 8:
		r = 3
	elif a == 4:
		r = 2
	elif a == 2:
		r = 1
	elif a == 1:
		r = 0
	return r

# horizontal value. 7 is the left-most as oriented in the stand
uh.set_layout(uh.PHAT)
uh.brightness(0.2)

wxVar = weather()

#def showLed():
while True:
	timeStr = time.strftime("%H%M%S")+str(wxVar)
	h = 7
	for f in timeStr:
	# run function to get the binary digits to light up for each section of the time
		x = findBinary (int(f))
		for y in x:
	# converts those array values into the actual values on the LED grid
			z = selectLed(y)
			uh.set_pixel(h, z, 255, 0, 0)
	# decrement horizontal value to keep moving to the right
		h -= 1
	uh.show()
	time.sleep(1.0)
	uh.off()

#time.sleep(20)
#uh.off()

#if __name__ == '__main__':
#	showLed()
