# pi-led-projects
Python scripts to control Pi Zero LED array

Notes:

  *Email checker needs Google json credentials which aren't synced.
  ```https://developers.google.com/workspace/guides/create-credentials#oauth-client-id
  The application type should be Desktop app.
  Download the JSON file, rename it to client_secret.json, and place it in the same path as the Python script
  ```

  *Weather script needs API key (in separate file) which isn't synced.

  *All scripts have to be run with sudo.
  
  *Install httplib2 (sudo apt install python-httplib2) and:
  ```
  sudo pip install -U setuptools
sudo pip install google-api-python-client
sudo pip install oauth2client
```

  *Web server runs with [Flask](http://flask.pocoo.org/docs/0.12/installation/#installation) (install it with sudo). To run the server (and yes, it has to be run as root):
```
export FLASK_APP=/home/pi/pi-led-projects/webserver.py
flask run --host=0.0.0.0
```
