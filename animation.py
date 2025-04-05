import time, os

def animate_ascii(frames, delay=0.2):
    """Animates a sequence of ASCII art frames in the terminal.

    Args:
        frames: A list of strings, where each string represents an ASCII art frame.
        delay: The time delay (in seconds) between frames.
    """
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
        print(frame)
        time.sleep(delay)

# if __name__ == "__main__":
#     # Define animation frames (example: a simple rotating line)
#     frames = [
#         "/",
#         "-",
#         "\\",
#         "|"
#     ]


frames = [
    '''

    |
        
    ''',
    '''

    | |
    
    ''',
    '''

    | | |

    ''',
    '''

    | | |
    
    | 
    ''',
    '''

    | | |
    
    | |
    ''',
    '''

    | | |
    
    | | |
    ''',
    '''
    /
    | | |
    
    | | |
    ''',
    '''
    / \\
    | | |
    
    | | |
    ''',
    '''
     / \\
    | | |
    
    | | |
    \\
    ''',
    '''
     / \\
    | | |
    
    | | |
    \\  /
    ''',
    '''
     / \\
    | | |
        /
    | | |
    \\  /
    ''',
    '''
     / \\
    | | |
     / /
    | | |
    \\  /
    ''',
            '''
     / \\
    | | |
     / /
    | | |
    \\  /
    ''',
        '''
     / \\
    | | |
     / /
    | | |
    \\  /
    ''',
        '''
     / \\
    | | |
     / /
    | | |
    \\  /
    '''
]

# Repeat frames to create a longer animation
animation_frames = frames * 3

# Animate the frames
# animate_ascii(animation_frames)