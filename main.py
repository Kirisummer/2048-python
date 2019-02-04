# sys.argv to process cli args
import sys
# atexit.register() to call the end() function
import atexit
# script's own functions for the game to run
import functions as funcs

# imports for different interfaces
if len(sys.argv)<2 or sys.argv[1]!='gui':
    import draw_cli as draw
else:
    import draw_pygame as draw

# initialising point count to zero
points=0

# function to run at script's exit. It calls draw.end() to terminate interface and
# prints score summary
def end():
    draw.end()
    print("You scored "+str(points)+" points.")
#registering the function to run at script's exit
atexit.register(end)

# initialising a field
# Function asks about the field size and then creates a NxN field, filled with
# zeroes, where N is size of field
field=funcs.init_field()
# Initialising a screen to print output to. Calls draw.init() function to do it
screen=draw.init()
# Main loop, which lasts until a player loses
while not funcs.lose(field):
    # Generating some number (2 or 4)
    funcs.gen(field)
    # Updating the interface with new field values. Calls draw.update() with
    # screen and field args
    draw.update(screen,field)
    # Getting and processing user input. Calls draw.process() with screen and field
    # args. Function has to return new field and points got from actions
    (field,points_got)=draw.process(screen,field)
    # Adding points achieved from action to points previouly gotten
    points+=points_got
