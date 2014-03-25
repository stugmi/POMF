#!/usr/bin/python2

###
#** You need to install 
#* python2-requests
#* python2-notify
#* xclip
#* scrot
###


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
from sys import argv
import getopt

### Edit ###

#Api for goatshot / pomf.cat 
api = ""


#Paths
screenshot_dir = "/tmp/"

#pomf.se
#image_directory = "http://a.pomf.se/"
#upload_script = "http://pomf.se/upload.php"

#goatshot / pomf.cat
image_directory = "http://i.pomf.cat" #More to come
upload_script = "http://s.pomf.cat/upload.php?apikey={}".format(api)

#Configs
notifyme = True
goatshot = True

############

def main():
	if image_upload == True:
		file_upload = "{0}{1}.png".format(screenshot_dir, int(time.time()))
		p = subprocess.Popen(["scrot", "--select", file_upload])
		p.wait()


	try:
	    if not os.path.exists(screenshot_dir):
		os.makedirs(screenshot_dir)

	except Exception as e:
	    notify("Error creating directory {0}, {1}".format(screenshot_dir), e)
	    exit()

	try:
	    response = requests.post(
                url=upload_script,
		files={"files[]":open(file_upload, "r")}
	        )
	except Exception as e:
	    print("Error uploading {0}".format(e))
	    main()
	
	if goatshot == True:
		response_text = response
	else:
	    response = response.text.split('"')
	    response_text = response[17]
	 	

        if notifyme == True:
        	notify(image_directory + response_text)
	clipboard(image_directory + response_text)
	print image_directory + response_text


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

def Usage():
    print "Usage: pomf [OPTION]... [FILE]\n"
    print "  -f, --file \tUploads a file to pomf.se"
    print "  -i, --image \tUploads a image using scrot --select and uploads the image to pomf.se"
    print "\n Example:\n\t pomf -f pomf.flac"
    print " \t Uploads a file via scrot --select and notifies you once it's done.\n"
    exit()

if len(argv) == 1:
	Usage()

try:
	opts, args = getopt.getopt(argv[1:], "hif", ["help", "image","file="])
except getopt.GetoptError, err:
	print("Error! Argument is invalid\n")
	Usage()

for o, a in opts:
	if o in ("-h","--help"):
		Usage()
	elif o in ("-i","--image"):
		image_upload = True
	elif o in ("-f","--file"):
		file_upload = argv[2]
	else:
		Usage()


if __name__ == "__main__":
   main()
