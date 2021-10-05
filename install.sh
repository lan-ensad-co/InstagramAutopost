#!/bin/bash

# run this script as sudo 
# to install all needed libs for igAutoPoster.py
if [[ "$EUID" != 0 ]]; then
    echo "this script must run as sudo !"
    exit
fi

sudo apt install python3 idle3
sudo apt install python3-pip
sudo apt install libopenjp2-7 #for Pillow (necessary)

python3 -m pip install picamera
python3 -m pip install Pillow
python3 -m pip install Flask
python3 -m pip install emojis
python3 -m pip install instabot

echo "lib install done !"
