# Team AI-Migos -- Loading/Unloading and Balancing of Containers on X2 Class Ship

# IMPORTS: libraries to use in code
import numpy as np # fast, efficient arrays, and calculations
import re # regex
import time # performance, error timeout
from datetime import datetime # for log file print

# Log file setup
log_file_to_write = "KeoghLongBeach" + str(datetime.now().year) + ".txt"
log_file = open(log_file_to_write, "a") # log file variable in use in all functions
user_name = "123" # user who signs in, "123" signifies no previous user signed in (first run)

#FUNCTION: all functions below
def log_file_init(): # determine if the user wants the log file restarted when programs starts
    global log_file
    choice = input("Do you want to restart the log file? y for yes, n for no\n-> ")
    while choice != "y" and choice != "n":
        choice = input("Do you want to restart the log file? y for yes, n for no\n-> ")
    if choice == "y":
        open(log_file_to_write, 'w').close() # clear file
    return

# Helper with log file printing [Month Day, Year:] (no appending space)
def get_date_time():
    return f"{datetime.now().strftime('%B')} {datetime.now().day}, {datetime.now().year}: {datetime.now().hour:0>2}:{datetime.now().minute:0>2}"

def log_file_change_user():
    global log_file, user_name
    if user_name != "123": # if there is a previous user, sign them out
        log_file.write(f"{get_date_time()} {user_name} signs out\n")
    user_name = input("Enter the name of the User to sign in\n-> ") # new user
    log_file.write(f"{get_date_time()} {user_name} signs in\n")
    return

def log_file_enter_comment():
    global log_file
    comment = input("Enter comment to append to log file\n-> ")
    log_file.write(f"{get_date_time()} {comment}\n")
    return

# Load/Unload
# 1 minute within ship, 2 minutes to truck, 4 minutes ship/buffer
def load_unload_ship(arr, op):
    if op == "l": # load 
        c_name = input("Enter exact name of container to load.\n-> ") # container name to move
        c_weight = int(input("Enter weight of container\n-> ")) # container weight
        cell_to_insert = [c_name, c_weight]
        # search for least time to insert
        least_time = float('inf')
        best_loc = [-1,-1]
        for col in range(1, 13):
            i = 8
            if arr[r(8)][c(col)][0] != "UNUSED": # check if top of column is already full
                continue
            while i > 1 and arr[r(i-1)][c(col)][0] == "UNUSED":
                i -= 1
            curr_time = (8 - i) + (col - 1)
            if curr_time < least_time:
                least_time = curr_time
                best_loc = [i, col]
        arr[r(best_loc[0])][c(best_loc[1])] = cell_to_insert # optimal location to place container [time]
        log_file.write(f"{get_date_time()} \"{c_name}\" is onloaded\n") # log file onloading
    elif op == "u": # unload 
        c_name = input("Enter exact name of container to offload.\n-> ") # container name to move
        move_c(arr, [c_name, 0], -1, -1) # loc == -1 to unload
        log_file.write(f"{get_date_time()} \"{c_name}\" is offloaded\n") # log file offloading
    return

# Balance ship: Heavier side of ship is no more than 10%
# weight of lighter side
def balance_ship(arr):
    # Get weight on both sides
    l_cells = []
    r_cells = []
    l_w = 0
    r_w = 0
    for i in range(1,9):
        for j in range(1,13):
            cell = arr[r(i)][c(j)] 
            if(cell[1] > 0):
                if j <= 6: # left side
                    l_cells.append(cell + [j])
                    l_w += cell[1] 
                else: # right side
                    r_cells.append(cell + [j])
                    r_w += cell[1]
    
    s_time = time.time()
    while (check_unbalance(l_w, r_w)): # while the ship is legally unbalanced
        if l_w > r_w: # move left -> right
            l_w -= l_cells[0][1]
            r_w += l_cells[0][1]
            temp = l_cells[0]
            l_cells.pop(0)
            r_cells.append(temp)
        else: # move right -> left
            r_w -= r_cells[0][1]
            l_w += r_cells[0][1]
            temp = r_cells[0]
            r_cells.pop(0)
            l_cells.append(temp)
        
        # check if timeout (balance not possible)
        if(time.time() - s_time >= 5):
            print("\n\nBalance not possible -_- PERFORM SIFT (put all containers in buffer zone, heaviest switch back and forth till row is filled, move up)\n\n")
            log_file.write(f"{get_date_time()} The ship is not able to be balanced in its current state. The operator must perform SIFT.\n") # log file balancing fail
            perform_sift(arr)
            log_file.write(f"{get_date_time()} SIFT has been completed.\n") # log file balancing fail
            return
    
    # Balance is possible, determine which cells have to move to the other side
    to_move_right = []
    for cell in r_cells:
        if cell[2] <= 6:
            cell.pop()
            to_move_right.append(cell)
    to_move_left = []
    for cell in l_cells:
        if cell[2] > 6:
            cell.pop()
            to_move_left.append(cell)
    
    for cell in to_move_right: 
        move_c(arr, cell, 7, 1)
    for cell in to_move_left:
        move_c(arr, cell, 6, -1)
    
    print("\nContainers to move to the left [port]:",to_move_left,"\n")
    print("Containers to move to the right [starboard]:",to_move_right,"\n")
    # print("Moved Containers: \n\n",arr)
    log_file.write(f"{get_date_time()} The ship has been balanced according to the legal definition of balancing.\n") # log file balancing success
    
# Helper to balance_ship function
# Returns false if the two sides of ship are balanced;; true otherwise.
def check_unbalance(l_w, r_w): 
    if l_w == r_w:
        return False
    max_side = max(l_w,r_w)
    min_side = min(l_w,r_w)
    return (((max_side - min_side) / max_side) > 0.1)

# Helper for balance/load optimal move for container [recursive]
# 1 minute within ship, 2 minutes to truck, 4 minutes ship/buffer
# cell is to be moved, loc is column to start with, mod is to either move right (+1) or move left (-1) 
# if loc is -1, cell is to be unloaded (removed from ship array)
def move_c(arr, cell, loc, mod):
    row_c,cell_c = find_cell(arr, cell) # get cell's index
    i = 8 # current row number
    while i != row_c: # loop down column to cell, move other containers out of the way
        curr_cell = arr[r(i)][c(cell_c)]
        if curr_cell[0] != "UNUSED" and curr_cell[0] != "NAN":
            out_bound = -1
            if (cell_c - mod <= 0) or (cell_c - mod >= 13): # so recurs loc doesn't go out of bounds
                out_bound = 1
            move_c(arr, curr_cell, cell_c + (mod * out_bound), mod * out_bound)
        i -= 1
    # here, access to container with nothing above, time to move to loc column
    # make current cell UNUSED
    arr[r(i)][c(cell_c)] = ["UNUSED", 0]
    if loc == -1: # if container is to be unloaded
        return
    # check that no column from cell_c to loc is completely full
    # if any are, move the top container out of the way
    for col in range(cell_c + mod, loc + mod):
        if arr[r(8)][c(col)][0] != "UNUSED":
            move_c(arr, arr[r(8)][c(col)], col + mod, mod)
    # get to loc column
    while cell_c != loc:
        if arr[r(i)][c(cell_c + mod)][0] == "UNUSED": # move mod column if possible
            cell_c += mod
        else: # move up 
            i += 1
    # then move as far down as possible, meaning when the cell below is not UNUSED
    while i > 1 and (arr[r(i-1)][c(cell_c)][0] == "UNUSED"):
        i -= 1
    # place the cell at [i, cell_c]
    arr[r(i)][c(cell_c)] = cell

    return # cell has been successfully moved

# Helper for move_c to return arr index of cell
# cell is guaranteed to be in arr
def find_cell(arr, cell):
    for i in range(1,9):
        for j in range(1,13):
            if arr[r(i)][c(j)][0] == cell[0]: # match
                return i,j
    return None # not possible to reach

# i is row user space, return row matrix space
def r(i):
    return 8-i

# i is column user space, return column matrix space
def c(i):
    return i-1

# perform SIFT on the ship
# put all containers in buffer zone, heaviest switch back and forth till row is filled, move up
def perform_sift(arr):
    buffer = []
    return 

def write_new_manifest(f_to_write, arr):
    open(f_to_write, 'w').close() # clear file
    f = open(f_to_write, "a")
    for i in range(1, 9):
        for j in range(1, 13):
            col = "0" + str(j) if j < 10 else str(j)
            cell = arr[r(i)][c(j)]
            l_write = f"[0{i},{str(j):0>2}], {{{str(cell[1]):0>5}}}, {cell[0]}"
            f.write(l_write)
            if i != 8 or j != 12: # not last line
                f.write("\n")
    f.close()
    # log file manifest finished 
    log_file.write(f"{get_date_time()} Finished a Cycle. Manifest {f_to_write} was written to desktop, and a reminder pop-up to operator to send file was displayed." + "\n") 
    return

def manifest_init():
    file_name = input("Enter the name of the manifest file. Example: SSMajestic.txt\n-> ")
    new_filename = file_name.split(".")[0] + "OUTBOUND.txt" # for updated manifest file
    # file_name = "ship_unbalanceable.txt"
    with open(file_name) as f:
        lines = f.readlines()

    # [8x12] grid, bottom left [1,1], top right [8,12] ;; arr[i][j] = [Name, Weight]
    arr = np.empty([8,12], dtype='object') # Ship grid with Containers and weights
    # populate ship_arr with Container [Name, weight]
    # vals is list: [row, column, weight, name]
    container_cnt = 0 # for log file manifest open message
    for line in lines:
        vals = [int(s) for s in re.findall(r'\b\d+\b', line)] + [line.split(",")[-1].strip()]
        arr[r(vals[0])][c(vals[1])] = [vals[3], vals[2]]
        if vals[2] > 0:
            container_cnt += 1
    log_file.write(f"{get_date_time()} Manifest {file_name} is opened, there are {container_cnt} containers on the ship\n") # log file open manifest message
    print(arr)
    
    return new_filename, arr

# MAIN: method below
# Log file initialization
log_file_init()
log_file_change_user()

# READ: the manifest file
new_filename, arr = manifest_init()

while(1):
    op = input("l for load, u for unload, b for balance, s for change user, c for adding user comment to log file, p for finishing the current manifest and open a new one, q for quit.\n-> ")
    if op == "l" or op == "u":
        load_unload_ship(arr, op)
    elif op == "b":
        balance_ship(arr)
    elif op == "s":
        log_file_change_user()
    elif op == "c":
        log_file_enter_comment()
    elif op == "p":
        write_new_manifest(new_filename, arr)
        new_filename, arr = manifest_init()
    elif op == "q":
        # create updated manifest file
        # log file write that cycle has finished
        write_new_manifest(new_filename, arr)
        log_file.write(f"{get_date_time()} {user_name} signs out\n")
        log_file.close()
        break

    print(arr)

