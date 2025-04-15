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
 @@@@@@@@@@@@@@@/      \\@@@/   @
@@@@@@@@@@@@@@@@\\      @@  @___@
@@@@@@@@@@@@@ @@@@@@@@@@  | \\@@@@@
@@@@@@@@@@@@@ @@@@@@@@@\\__@_/@@@@@
 @@@@@@@@@@@@@@@/,/,/./'/_|.\\'\\,\\
   @@@@@@@@@@@@@|  | | | | | | | |
                 \\_|_|_|_|_|_|_|_|'''

frames = [
    '''
              O
    | ^ | X | ^ | X | ^ |
    |   |   |   |   |   |
    ''',
    '''
              O
    |   | ^ | X | ^ | X |
    |   |   |   |   |   |
    ''',
        '''
              O
    | X |   | ^ | X | ^ |
    |   |   |   |   |   |
    ''',
        '''
              O
    | ^ | X |   | ^ | X |
    |   |   |   |   |   |
    ''',
            '''
              O
    | X | ^ | X |   | ^ |
    |   |   |   |   |   |
    ''',
            '''
              O
    | ^ | X | ^ | X |   |
    |   |   |   |   |   |
    ''',
]
win = [
        '''
              O
    | ^ | X |   | ^ | X |
    |   |   |   |   |   |
    ''',
            '''
              
    | ^ | X | O | ^ | X |
    |   |   |   |   |   |
    ''',
        '''
              
    | ^ | X |   | ^ | X |
    |   |   | O |   |   |
'''
]
delay = 1.00
# count the frames, return numbers to list
def cel_maker(frames):
    frame_count = len(frames)
    frame_ints = []
    for i in range(frame_count):
        frame_ints.append(i)
     # create list of tuples of frame, frame (zip returns zip object. list to convert.)
    cels = zip(frames, frame_ints)
    cels = list(cels)
    return cels

# make the animations
main_animation = cel_maker(frames) * 100
win_animation = cel_maker(win)

# create the win animation
def winAnimation():
    for frame in win_animation:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You deftly manuveur through an empty space in the molten meat conveyor belt.")
        print(frame[0])
        time.sleep(delay)

key_pressed = False  # Global flag to track keypress

def on_key_event(event):
    global key_pressed
    if event.name == "a":  # Check if the "A" key was pressed
        key_pressed = True

keyboard.hook(on_key_event)  # Hook the keypress event

def game_loop(cels):
    global key_pressed
    target_index = (len(cels) // 2) / 100  # Target index is halfway through the frames
    for frame, index in cels:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
        print("Press A when it's safe to pass!")
        # print(f"Current Index: {index}, Target Index: {target_index}")
        print(frame)

        # Reset key_pressed for each frame
        key_pressed = False
        start_time = time.time()
        while time.time() - start_time < delay:
            if key_pressed and index == target_index:
                winAnimation()
                return
            elif key_pressed:
                print(f"{skull}")
                print("You lose!")
                time.sleep(2.0)
                exit()
                

        # Continue to the next frame after the delay


