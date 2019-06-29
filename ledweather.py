import pyowm
from modules import owmapikey
def weather():

	owm = pyowm.OWM(owmapikey.strApiKey)
	w = owm.weather_at_id(5134693)
	wd = w.get_weather()
	tempF = int(wd.get_temperature('fahrenheit')['temp'])
#	print (tempF)
	return tempF

if __name__ == '__main__':
	weather()
