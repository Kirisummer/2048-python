# Functions to use in creating interfaces are marked with (*)

# Remove all zeroes found in line
def rm_zero(line):
    i=0
    while(i<len(line)):
        if line[i]==0:
            del line[i]
            i=0
            continue
        i+=1

# Push zeroes to the back of line until it is full
def put_zero(line,size):
    for i in range(len(line),size):
        line.append(0)

# Shift the line to the left
def shift_left(line):
    # Variable to indicate which numbers are already merged
    lock=0
    # Points aquired from shift
    # Calculated as sum of the merged numbers
    points=0
    while True:
        # Copy the line to check for changes later
        line_cp=line.copy()
        # Remove all the zeroes in line (they will return later)
        rm_zero(line)
        # Repeat for each element of the line but the first:
        for i in range(1,len(line)):
            # If element being checked is already merged, skip to the next
            if lock>=i:
                continue
            # If element to the left is equal to the current elements,
            # merge current element with one to the left and set current to zero.
            # Adding the points by the rule above and starting over from the 
            # first element, just for safety
            if line[i]==line[i-1]:
                line[i-1]*=2
                line[i]=0
                lock=i
                points+=line[i-1]
                break
            # Fixate current element as merged (it cannot be changed)
            else:
                lock=i
        # Fill the rest of the line with zeroes (I told you, they have returned :D)
        put_zero(line,len(line_cp))
        # If there were no changes, break out of the loop
        if line_cp==line:
            break
    # Return the amount of points achieved from shift
    return points

# Transpose the field
def row_to_collumn(field):
    # Making the empty resulting field
    res=[]
    # Append each collumn to resulting field as the row
    for i in range(0,len(field)):
        collumn=[]
        for line in field:
            collumn.append(line[i])
        res.append(collumn)
    return res

# Rotate the field to the left
def rot_l(field):
    field_cp=field.copy()
    res=field.copy()
    # Reverse each line of the field...
    for i in range(len(field_cp)):
        field_cp[i]=field_cp[i][::-1]
    # ...and transpose that field 
    res=row_to_collumn(field_cp)
    return res

# Rotate the field to the right
def rot_r(field):
    # Just rotate the field to the left three times
    res=field.copy()
    for i in range(3):
        res=rot_l(res)
    return res

# Shift each row of the field left (*)
# Returns a new field and amount of points aquired from the shift in a tuple
def left(field):
    for line in field:
        points=shift_left(line)
    return (field,points) # not nessesary to return field, as field wasn't given any value in a function
                 # just for consistency with other direction functions

# Shift each row of the field right (*)
# Returns a new field and amount of points aquired from the shift in a tuple
def right(field):
    # Reverse each row, shift it to the left and reverse it again
    for i in range(0,len(field)):
        field[i]=field[i][::-1] # reverse a line
        points=shift_left(field[i])
        field[i]=field[i][::-1]
    return (field,points) # same here, just for consistency

# Shift each collumn of the field up (*)
# Returns a new field and amount of points aquired from the shift in a tuple
def up(field):
    # Rotate the field to the left, shift the field left and 
    # rotate it to the right
    field=rot_l(field)
    (field,points)=left(field)
    field=rot_r(field)
    return (field,points) # the way the function is defined requires to return field because
                 # field is assigned to another object

# Shift each collumn of the field down (*)
# Returns a new field and amount of points aquired from the shift in a tuple
def down(field):
    # Rotate the field to the right, shift the field left and
    # rotate it to the right
    field=rot_r(field)
    (field,points)=left(field)
    field=rot_l(field)
    return (field,points) # same here
