import os
from flask import Flask
app = Flask(__name__)

@app.route("/<float:brightness>")
def b(brightness):
        #s="sudo su -c 'echo {} >/sys/class/backlight/intel_backlight/brightness'".format(brightness)
        s="xrandr --output LVDS-1 --brightness {}".format(brightness)
        print(s)
        os.system(s)
        return "Ok!"

@app.route("/")
def hello():
        return "Hello World!"
