import time
import random
import unicornhat as uh

uh.set_layout(uh.PHAT)
uh.brightness(0.7)

for x in range(8):
	for y in range(4):
		a = random.randint(0, 255)
		b = random.randint(0, 255)
		c = random.randint(0, 255)
        	uh.set_pixel(x, y, a, b, c)
uh.show()
time.sleep(5)
