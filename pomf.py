#!/usr/bin/env python2

'''
Originally made by Jirx, modified for pomf.se 

** You need to install 
* python2-requests
* python2-notify
* xclip
* scrot

'''


try:
    import requests
except ImportError:
    exit("Install python2-requests")
try:
    import pynotify
except ImportError:
    exit("Install python2-notify")
import os
import subprocess
import time

screenshot_dir = os.getenv("HOME") + os.path.sep + "screenshots" + os.path.sep
image_directory = "http://a.pomf.se/"
upload_script = "http://pomf.se/upload.php"

def notify(message):
	pynotify.init(message)
	notifyme=pynotify.Notification (message)
	notifyme.show ()

def clipboard(message):
	p = subprocess.Popen(
		["xclip", "-selection", "c"],
		stdout=subprocess.PIPE,
		stdin=subprocess.PIPE
	)
	p.stdin.write(message)

try:
	if not os.path.exists(screenshot_dir):
		os.makedirs(screenshot_dir)

except Exception as e:
	notify("Error creating directory {0}, {1}".format(screenshot_dir), e)
	exit()

screenshot_name = "{0}{1}.png".format(screenshot_dir, int(time.time()))

p = subprocess.Popen(["scrot", "--select", screenshot_name])
p.wait()

try:
	response = requests.post(
		url=upload_script,
		files={"files[]":open(screenshot_name, "r")}
	)
except Exception as e:
	notify("Error uploading {0}".format(e))
	exit()

response = response.text.split('"')
response_text = response[9]

notify(image_directory + response_text)
clipboard(image_directory + response_text)
