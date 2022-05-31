#!/bin/bash

# run this script as sudo 
# to install all needed libs for igAutoPoster.py
if [[ "$EUID" != 0 ]]; then
    echo "this script must run as sudo !"
    exit
fi

sudo apt install python3 idle3 python3-pip libopenjp2-7 libtiff5

python3 -m pip install picamera Pillow Flask emojis instabot

echo "lib install done !"
