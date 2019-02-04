# For generating random element for gen() with random.randint()
import random

# Initialise the field: ask about the field size, create zero-filled field of
# given size
def init_field():
    size=int(input("Enter the playfield size: "))
    field=[]
    for i in range(0,size):
        field.append([])
        for j in range(0,size):
            field[i].append(0)
    return field

# Generate 2 (always available) or 4 (only if there is element greater or equal 
# to 8
def gen(field):
    # Find the greatest element of the field
    maximum=max(field[0])
    for line in field:
        max_tmp=max(line)
        if max_tmp<maximum:
            maximum=max_tmp
    # If there is an element greater or equal to 8, randomly choose between 2 and 4
    if maximum>=8:
        elem=random.randint(1,2)*2 
    # or pick 2 otherwise
    else:
        elem=2

    # Randomly choose coordinates until empty place is found
    x=random.randint(0,len(field)-1)
    y=random.randint(0,len(field)-1)
    while field[y][x]!=0:
        x=random.randint(0,len(field)-1)
        y=random.randint(0,len(field)-1)
    field[y][x]=elem
    return field

# Check if the player lost <=> the field if full
def lose(field):
    # If there is no empty place on the field, the player lost
    for line in field:
        for elem in line:
            if elem == 0:
                return False
    return True
