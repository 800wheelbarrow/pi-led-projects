import time
import unicornhat as uh

uh.set_layout(uh.PHAT)
uh.brightness(0.5)

fulltime = time.localtime()
hour = int(time.strftime("%I"))
minute = int(time.strftime("%M"))

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

def flashMin():

        for h in range(0, minute):
                for x in range(8):
                        for y in range(4):
                                uh.set_pixel(x, y, 255, 0, 0)
                uh.show()
                time.sleep(0.5)
                uh.clear()
                uh.show()
                time.sleep(0.5)

def flashMinQ():

	if minute <= 15:
		minflash = 1
	elif minute <= 30:
		minflash = 2
	elif minute <= 45:
        	minflash = 3
	else:
        	minflash = 4

        for h in range(0, minflash):
                for x in range(8):
                        for y in range(4):
                                uh.set_pixel(x, y, 255, 0, 0)
                uh.show()
                time.sleep(1)
                uh.clear()
                uh.show()
                time.sleep(1)


if __name__ == '__main__':
	flashHour()
	flashMin()
