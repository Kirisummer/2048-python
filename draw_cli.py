# Example ncurses interface
### Mandatory functions are marked with (*). Main module depends on those ###
# You need mech module to access shifts, which you have to do manually
# Do not forget to import the module your interface depends on
import mech,curses

# Function to initialise screen (*)
# Has to return screen
def init():
    screen=curses.initscr()
    curses.noecho()
    curses.cbreak()
    return screen

# Update the screen with new field data (*)
def update(screen,field):
    screen.clear()
    for i in range(0,len(field)):
        for j in range(0,len(field)):
            screen.addstr(str(field[i][j])+' ')
        screen.addstr('\n')
    screen.refresh()

# Function to exit the game. Basically fills field with 1s to trigger funcs.lose()
# function
def quit(screen,field):
    screen.addstr("Exit? ")
    screen.refresh()
    if(chr(screen.getch())=='y'):
        for i in range(0,len(field)):
            for j in range(0,len(field)):
                field[i][j]=1
    return field


# Function to get and process user input (*)
# Has to return new field data and number of points aquired
# Usage and descriptions of action functions are in the mech module
def process(screen,field):
    c=chr(screen.getch())
    points=0
    # The following three lines copy field to field_cp
    field_cp=[]
    for line in field:
        field_cp.append(line.copy())

    if c=='h':
        (field,points)=mech.left(field)
    elif c=='j':
        (field,points)=mech.down(field)
    elif c=='k':
        (field,points)=mech.up(field)
    elif c=='l':
        (field,points)=mech.right(field)
    elif c=='q':
        field=quit(screen,field)
    else:
        screen.addstr("\nUse 'h', 'j', 'k', 'l' for moving left, down, up and right\nor 'q' to quit")
        screen.refresh()
        process(screen,field)

    # Checking if field changed. If not, process input again
    if field==field_cp:
        (field,points)=process(screen,field)

    return (field,points)


# Function to terminate the interface (*)
def end():
    curses.nocbreak()
    curses.echo()
    curses.endwin()
