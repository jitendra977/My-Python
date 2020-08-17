from time import struct_time
from typing import Union

import pygame
import datetime
import time


def getdate():
    import datetime
    return datetime.datetime.now()


def tone():
    from pygame import mixer

    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load("C:\\Users\\jiten\\Downloads\\Music\\music (3).mp3")

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()

    # infinite loop
    while True:

        print("\nPress [d] for I drank water, [c] for Can't drink water")
        print("Press 's' for stop the alarm always Exit application")
        query = input(" :- ")

        if query == 'd':
            with open("Health_log.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + "Drank Water I want healthy " + "\n")
                print(query, "Next remaining alarm for Exercise")

            # Pausing the music
            mixer.music.pause()
        elif query == 'c':
            with open("Health_log.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + "Can't drink water " + "\n")
                print(query, "Next remaining alarm for Exercise")
            # Resuming the music
            mixer.music.pause()
        elif query == "s":
            with open("Health_log.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + "Scoped this Alarm... " + "\n")
                print(query, "Stop always this Alarm...")
            # Stop the mixer
            mixer.music.stop()
            break


def star(func):
    def inner(*args, **kwargs):
        print("X" * 55)
        func(*args, **kwargs)
        print("X" * 55)

    return inner


@star
def printer(msg):
    print(msg)


def title():
    printer("-------------------OUR HEALTH SYSTEM-------------------")
    time.sleep(1)
    print("Loading...............", end="")
    time.sleep(1)
    print("..................", end="")
    time.sleep(1)
    print("..................", end="")


title()
hour_min = time.localtime()
if hour_min.tm_hour >= 9:
    if hour_min.tm_hour <= 17:
        if hour_min.tm_hour == 13 and hour_min.tm_min == 6:
            tone()
        elif hour_min.tm_hour == 12 and hour_min.tm_min == 45:
            tone()
        else:
            pass
    else:
        pass
else:
    pass


print("\nYour  Time:", hour_min.tm_hour, ":", hour_min.tm_min)

# while True:
#     print("retrieve old log press for [r] ")
#     retrieve = input(" 1 Run alarm  2 for  retrieve log ")
#     if retrieve=="1":
#             hour_min = time.localtime()
#             if hour_min.tm_hour >= 9:
#                 if hour_min.tm_hour <= 17:
#                     if hour_min.tm_hour == 12 and hour_min.tm_min == 36:
#                         tone()
#                     elif hour_min.tm_hour == 12 and hour_min.tm_min == 45:
#                         tone()
#                     else:
#                         continue
#
#                 else:
#                     break
#             else:
#                 break
#
#     elif retrieve == "2":
#         with open("Health_log.txt") as op:
#             for i in op:
#                 print(i, end="")
#     else:
#         continue
# print("\nYour Log Time:", hour_min.tm_hour, ":", hour_min.tm_min)['2020-08-14 13:06:56.628842']: I can't drink water.
