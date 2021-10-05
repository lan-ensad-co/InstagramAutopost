#this program need python Flask / piCamera / Pillow / emojis (pip install emojis) & instabot libraries

# when launch, server can be acessed thru http://local-ip:4040/takeapicandpost
#to tun the process of taking a picture, generating an emoji caption and posting to instagram
# >>>>> Olivain.art

import instabot
from picamera import PiCamera
from PIL import Image
import os
import time
import emojis
import random
import string
from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
LED = 7 # pin led
GPIO.setup(LED, GPIO.OUT)

app = Flask(__name__) # setup flask app (port 80)

#to generate a new image path
def genImagePath():
    random_string = ''
    maxChar = random.randint(3,15)
    str = string.ascii_lowercase
    for i in range(maxChar):
            random_string+=random.choice(str)
    random_string+=".jpg"
    curPath = os.path.dirname(os.path.abspath(__file__))
    fullPath = curPath+"/"+random_string;
    return fullPath

#to take and image from the pi camera
def takePicture(imgPath):
    #print("taking a picture")
    GPIO.output(LED, GPIO.HIGH)
    camera = PiCamera()
    camera.start_preview()
    #time.sleep(3)
    camera.capture(imgPath)
    GPIO.output(LED, GPIO.LOW)
    camera.stop_preview()

#to resize the picture
def resizePicture(imgPath, desiredHeight):
    print("resizing")
    im = Image.open(imgPath)
    fixed_height = desiredHeight
    height_percent = (fixed_height / float(im.size[1]))
    width_size = int((float(im.size[0]) * float(height_percent)))
    image = im.resize((width_size, fixed_height), PIL.Image.NEAREST)
    image.save(imgPath)

#to generate and genEmojiCaption
def genEmojiCaption():
    print("generating emojis caption..")
    fullCaption = ""
    emojisAllTags = list(emojis.db.get_tags())
    nbMaxEmojis = random.randint(1,9)
    print(nbMaxEmojis)
    for i in range(nbMaxEmojis):
        rndEmoji = emojis.db.get_emojis_by_tag(random.choice(emojisAllTags))
        for item in rndEmoji:
            fullCaption += item.emoji
            if(random.random(0,1) > 0):
                fullCaption+=" "
    return fullCaption

#to post the file on instagram thru instabot
def postPicture(u, p, imgPath, imgCaption):
    print("Posting to instagram")
    bot = Bot()
    bot.login(username=u, password=p, is_threaded=True)
    bot.upload_photo(imgPath, caption=imgCaption)
    print("OK")

#to delete a file
def delPicture(imgPath):
    os.remove(imgPath)

#to run the full process
@app.route('/takeapicandpost')
def fullProcessInstagramAutoPost():
    user_name = 'igAccount'
    password = 'password!'
    img = genImagePath()
    takePicture(img)
    #resizePicture(img,720)
    caption = genEmojiCaption()
    postPicture(user_name, password, img, caption)
    delPicture(img)
    return caption

#is this even necessary ? i think it is !
@app.route('/')
def nothing():
    return "nothing here..."

#run the process
if __name__ == '__main__':
    app.debug = False
    app.run(host = '0.0.0.0',port=4040) # access the server on http://local-IP:4040
