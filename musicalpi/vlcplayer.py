#!/usr/bin/env python3
from time import sleep
import logging
import os
import RPi.GPIO as GPIO
import random
import vlc

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

sleep_time = 10
path = "/home/pi/Music/musicalpi/"


def music_file(parth): 
    return random.choice([ x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])

p = vlc.MediaPlayer("file://" + path +  music_file(path))

while True:
    amusic_file = music_file(path)

    if not GPIO.input(17):
        p = vlc.MediaPlayer("file://" + path + amusic_file)
        logging.debug(path + amusic_file)
        p.play()
        sleep(sleep_time)
        p.stop()
    else:
        p.stop()
