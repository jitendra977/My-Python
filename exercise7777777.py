from time import struct_time
from typing import Union
from pygame import mixer
from datetime import datetime
from timeit import time
def tone_loop(tone,stop_key):
    mixer.init()
    mixer.music.load(tone)
    mixer.music.set_volume(2)
    mixer.music.play()
    while True:
        user_input=input("")
        if user_input==stop_key:
            mixer.music.stop()
            break
def log(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg},{datetime.now()},\n")
if __name__ == '__main__':
    routine = time.localtime()
    while True :
        if routine.tm_hour==14 and routine.tm_min==32:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            tone_loop('C:\\Users\\jiten\\Downloads\\Music\\music (4).mp3', 'drank')
            init_water = time()
            log("Drank Water at")
        if routine.tm_hour == 14 and routine.tm_min == 16:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            tone_loop('C:\\Users\\jiten\\Downloads\\Music\\music (4).mp3', 'drank')
            init_water = time()
            log("Drank Water at")
            routine.tm_min+1
