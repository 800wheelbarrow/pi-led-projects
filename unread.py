import time
import random
import unicornhat as uh
from modules import emailunread
uh.set_layout(uh.PHAT)
uh.brightness(0.7)

def flashUnread():
	z = emailunread.checkUnread()

	for d in range(0, z):
		for x in range(8):
			for y in range(4):
#		a = random.randint(0, 255)
#		b = random.randint(0, 255)
#		c = random.randint(0, 255)
        			uh.set_pixel(x, y, 80, 180, 30)
#	print d
		uh.show()
		time.sleep(0.5)
		uh.clear()
		uh.show()
		time.sleep(0.5)

if __name__ == '__main__':
	while True:
		time.sleep(10)
		flashUnread()
