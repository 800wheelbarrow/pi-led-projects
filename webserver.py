import randomlights
import timeflash
from flask import Flask
app = Flask(__name__)

@app.route('/')
def landing():
        return 'This is the Pi Zero web server.'

@app.route('/random')
def random():
	randomlights.randomLights();
	return 'Random lights complete.'

@app.route('/time')
def time():
        timeflash.flashAll();
        return 'Time flash complete.'
