# Using the same animation technique from animation.py
# Create a list of frame numbers from frames list
# If player input is received within correct frame # range
# Player successfully passes obstacle
# If not: -2 Stamina & try again

import time, os, keyboard

skull = '''
       @@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@/      \@@@/   @
@@@@@@@@@@@@@@@@\      @@  @___@
@@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@
@@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@
 @@@@@@@@@@@@@@@/,/,/./'/_|.\'\,\\
   @@@@@@@@@@@@@|  | | | | | | | |
                 \_|_|_|_|_|_|_|_|'''

treasure = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************'''

frames = [
    '''
    |   |   |   |   |   |
    | X | X |   | X | X |
    |   |   |   |   |   |
    ''',
    '''
    | o |   |   |   |   |
    | X | X |   | X | X |
    |   |   |   |   |   |
    ''',
        '''
    |   | o |   |   |   |
    | X | X |   | X | X |
    |   |   |   |   |   |
    ''',
        '''
    |   |   | o |   |   |
    | X | X |   | X | X |
    |   |   |   |   |   |
    ''',
            '''
    |   |   |   | o |   |
    | X | X |   | X | X |
    |   |   |   |   |   |
    ''',
            '''
    |   |   |   |   | o |
    | X | X |   | X | X |
    |   |   |   |   |   |
    ''',
]

win_animation = [
        '''
    |   |   | o |   |   |
    | X | X |   | X | X |
    |   |   |   |   |   |
    ''',        '''
    |   |   |   |   |   |
    | X | X | o | X | X |
    |   |   |   |   |   |
    ''',
        '''
    |   |   |   |   |   |
    | X | X |   | X | X |
    |   |   | o |   |   |
    ''',


]
# count the frames, return numbers to list
frame_count = len(frames)
frame_ints = []
for i in range(frame_count):
    frame_ints.append(i)

# create tuples of frame, frame #
cels = zip(frames, frame_ints)
cels = list(cels)
# Repeat frames to create a longer animation
animation_loops = cels * 100

# Animate the frames
def animation_loops(frames, delay=0.25):
    """Animates a sequence of ASCII art frames in the terminal.

    Args:
        frames: A list of strings, where each string represents an ASCII art frame.
        delay: The time delay (in seconds) between frames.
    """
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
        print("Press and hold A when it's safe to pass!")
        print(frame[0])
        time.sleep(delay)
        if keyboard.is_pressed("a") and frame[1] == 3:
            print(f"{treasure}{frame[1]}")
            break
        elif keyboard.is_pressed("a"):
            print(f"{skull}{frame[1]}")
            break


animate_ascii(animation_loops)