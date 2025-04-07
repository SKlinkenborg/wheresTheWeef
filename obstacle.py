# Using the same animation technique from animation.py
# Create a list of frame numbers from frames list
# If player input is received within correct frame # range
# Player successfully passes obstacle
# If not: -2 Stamina & try again

import time, os, keyboard, math

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
win = [
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
delay = 1.25
# count the frames, return numbers to list
def cel_maker(frames):
    frame_count = len(frames)
    frame_ints = []
    for i in range(frame_count):
        frame_ints.append(i)
     # create tuples of frame, frame #
    cels = zip(frames, frame_ints)
    cels = list(cels)
    return cels

# create list of tuples for each animation
main_animation = cel_maker(frames) * 100
win_frames = cel_maker(win)

def winAnimation():
    for frame in win_frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You win!!!")
        print(frame[0])
        time.sleep(delay)

def game_loop(cels):
    for frame, index in cels:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
        print("Press A when it's safe to pass!")
        print(index)
        print(frame)
        # Non-blocking delay loop
        start_time = time.time()
        while time.time() - start_time < delay:
            if keyboard.is_pressed("a") and index == int(math.ceil(len(cels) / 2) / 100):
                winAnimation()
                return
            elif keyboard.is_pressed("a"):
                print(f"{skull}")
                return

        # Continue to the next frame after the delay


while True:
    game_loop(main_animation)
    break