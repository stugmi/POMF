#POMF.py
POMF.py is a simple script for uploading images and files to http://pomf.se

The script creates a folder "screenshots" in your home directory where all screenshots are saved.


##You need to install
* python2-requests
* python2-notify
* xclip
* scrot



##How to use
```
pomf -i           Uses scrot -s to select an area or window. To select an area just click and drag. 
                  Select window or whole desktop you simply just click
                  
pomf -f file      Uploads specified file to pomf.se and returns URL
```
