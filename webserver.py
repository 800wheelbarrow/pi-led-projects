import randomlights
import timeflash
import weather2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def landing():
        return '<p>This is the Pi Zero web server.</p><p><a href="/random">Random</a></p><p><a href="/time">Time</a></p><p><a href="/weather">Weather</a></p>'

@app.route('/random')
def random():
	randomlights.randomLights();
	return 'Random lights complete.'

@app.route('/time')
def time():
        timeflash.flashAll();
        return 'Time flash complete.'

@app.route('/weather')
def wea():
        weather2.weather();
        return 'Weather flash complete.'
