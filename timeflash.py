import time
import unicornhat as uh

uh.set_layout(uh.PHAT)
uh.brightness(0.5)

fulltime = time.localtime()
hour = int(time.strftime("%I"))
minute = time.strftime("%M")
minleft = int(minute[0])
minright = int(minute[-1])

def flashHour():

	for h in range(0, hour):
		for x in range(8):
			for y in range(4):
    				uh.set_pixel(x, y, 0, 0, 255)
		uh.show()
		time.sleep(0.5)
		uh.clear()
		uh.show()
		time.sleep(0.5)

def flashMinLeft():

        for h in range(0, minleft):
                for x in range(8):
                        for y in range(4):
                                uh.set_pixel(x, y, 255, 0, 0)
                uh.show()
                time.sleep(0.5)
                uh.clear()
                uh.show()
                time.sleep(0.5)

def flashMinRight():

       for h in range(0, minright):
                for x in range(8):
                        for y in range(4):
                                uh.set_pixel(x, y, 0, 255, 0)
                uh.show()
                time.sleep(0.5)
                uh.clear()
                uh.show()
                time.sleep(0.5)

if __name__ == '__main__':
	flashHour()
	flashMinLeft()
	flashMinRight()
