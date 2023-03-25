import tkinter as tk
from tkinter import filedialog
import datetime
import time
import os
from container_load_balance import *

#Get current year
#Used for creating log file
today = datetime.date.today()
current_year = today.year
full_name = ""
previous_instructions = []
# Log file setup
log_file_to_write = ""
current_container = ""
current_operation = ""
current_manifest = ""

#frame 0
def program_start():

        # Clear the existing widgets in the frame
        for widget in frame.winfo_children():
            widget.destroy()

        def check_name():
            if full_name=="":
                prompt_label.config(text="No user signed in. Please try again\nPress CTRL + 'S' to sign in, or click on the 'Actions' dropdown", fg='red')
            else:
                start_a_new_log_file_prompt()


        # Add a label to the frame with the welcome message
        welcome_label = tk.Label(frame, text="Welcome!", font=("Helvetica", 18))
        welcome_label.pack(pady=50)

        # Add new log file prompt to the frame
        prompt_label = tk.Label(frame, text="Press CTRL + 'S' to sign in, or click on the 'Actions' dropdown", font=("Helvetica", 16))
        prompt_label.pack(pady=50)

        continue_button = tk.Button(frame, text="Continue", font=("Helvetica", 16), command=check_name)
        continue_button.pack(pady=50)

#frame 1
def start_a_new_log_file_prompt():

    message = f"Welcome!"

    # Clear the existing widgets in the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Add a label to the frame with the welcome message
    welcome_label = tk.Label(frame, text=message, font=("Helvetica", 18))
    welcome_label.pack(pady=50)

    # Add new log file prompt to the frame
    prompt_label = tk.Label(frame, text="Would you like to start a new log file?", font=("Helvetica", 16))
    prompt_label.pack(pady=50)

    # Add yes and no buttons to the frame
    button_frame = tk.Frame(frame)
    button_frame.pack()

    no_button = tk.Button(button_frame, text="No", font=("Helvetica", 16), command=load_existing_log_file) #shift frame
    no_button.pack(side=tk.RIGHT, padx=10)

    yes_button = tk.Button(button_frame, text="Yes", font=("Helvetica", 16), command=create_new_log_file)
    yes_button.pack(side=tk.LEFT, padx=10)

# Define functions for handling button clicks
#Frame 3
def create_new_log_file():
    # Code to create a new log file
    for widget in frame.winfo_children():
        widget.destroy()

    global log_file_to_write
    log_file_to_write = 'KeoghLongBeach.txt'

    welcome_label = tk.Label(frame, text=f"Creating default log file named '{log_file_to_write}'."
                                         "\nWould you like to append the current year?"
                                         f"\nCurrent Year: {current_year} ", font=("Helvetica", 18))
    welcome_label.pack(pady=50)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    back_button = tk.Button(button_frame, text="Back", font=("Helvetica", 16), command=start_a_new_log_file_prompt)
    back_button.pack(side=tk.LEFT, padx=10)

    no_button = tk.Button(button_frame, text="No", font=("Helvetica", 16), command=no_append_year)
    no_button.pack(side=tk.LEFT, padx=10)

    yes_button = tk.Button(button_frame, text="Yes", font=("Helvetica", 16), command=yes_append_year)
    yes_button.pack(side=tk.RIGHT, padx=10)

def yes_append_year():
    for widget in frame.winfo_children():
        widget.destroy()

    global log_file_to_write
    log_file_to_write = f'KeoghLongBeach{current_year}.txt'

    welcome_label = tk.Label(frame, text=f"Created default log file '{log_file_to_write}'.", font=("Helvetica", 18))
    welcome_label.pack(pady=50)

    # Continue
    continue_button = tk.Button(frame, text="Continue", font=("Helvetica", 16), command=upload_manifest)
    continue_button.pack(pady=50)

def no_append_year():
    for widget in frame.winfo_children():
        widget.destroy()

    welcome_label = tk.Label(frame, text=f"Created default log file 'KeoghLongBeach.txt'.",
                             font=("Helvetica", 18))
    welcome_label.pack(pady=50)

    # Continue
    continue_button = tk.Button(frame, text="Continue", font=("Helvetica", 16), command=upload_manifest)
    continue_button.pack(pady=50)

def resume():
    for widget in frame.winfo_children():
        widget.destroy()

    welcome_label = tk.Label(frame, text="This application has detected that the previous executation has been interrupted"
                                         "\nWould you like to resume the program?",
                             font=("Helvetica", 18))
    welcome_label.pack(pady=50)

    # Continue
    continue_button = tk.Button(frame, text="Continue", font=("Helvetica", 16), command=program_start())
    continue_button.pack(pady=50)

#frame 2
def load_existing_log_file():
    # Code to load an existing log file
    for widget in frame.winfo_children():
        widget.destroy()

    global log_file_to_write
    log_file_to_write = f'KeoghLongBeach{current_year}.txt'

    welcome_label = tk.Label(frame, text=f"Using default log file {log_file_to_write}.",
                             font=("Helvetica", 18))
    welcome_label.pack(pady=50)

    # Put the buttons in a new frame
    button_frame = tk.Frame(frame)
    button_frame.pack()

    back_button = tk.Button(button_frame, text="Back", font=("Helvetica", 16), command=start_a_new_log_file_prompt)
    back_button.pack(side=tk.LEFT, padx=10)

    continue_button = tk.Button(button_frame, text="Continue", font=("Helvetica", 16), command=upload_manifest)
    continue_button.pack(side=tk.LEFT, padx=10, pady=50)

def shorten_file(filename):
    file = os.path.split(filename)[1]
    return file

#takes file input
#frame 4
def upload_manifest():
    for widget in frame.winfo_children():
        widget.destroy()

    label = tk.Label(frame, text="Please upload a Manifest file",
                             font=("Helvetica", 18))
    label.pack(pady=50)

    selected_file = tk.Label(frame, text="No file selected",
                             font=("Helvetica", 18))
    selected_file.pack(pady=50)

    #bug needs to be patched here
    #filedialog.askopenfilename() allows the user to select multiple files
    # this means infinite continue buttons can be selected
    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])  # file path established
        if file_path:
            selected_file.config(text=f"Selected file: {file_path}")  # file input
            continue_button.pack(pady=50)
            # here is where interactions with backend start
            file_name = shorten_file(file_path)  # file_path truncated into txt file
            print(file_name)
            root.title("Mainfest: " + file_name)
            global file_arr
            file_arr = manifest_init(file_path)  # txt file passed into manifest_init to be transformed
            global current_manifest
            current_manifest = file_name
            # into arr
            num_containers = count_containers(file_arr)
            write_to_log_file(f"Manifest {file_name} is opened, there are {num_containers} containers on the ship", log_file_to_write)

    continue_button = tk.Button(frame, text="Continue", font=("Helvetica", 16), command=balance_or_transfer)
    button = tk.Button(frame, text="Select File", command=browse_file)
    button.pack(pady=50)

#frame 6
def balance_or_transfer():
    for widget in frame.winfo_children():
        widget.destroy()

    label = tk.Label(frame, text="Please select an operation",
                     font=("Helvetica", 18))
    label.pack(pady=50)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    balance_button = tk.Button(button_frame, text="Balance the ship", font=("Helvetica", 16), command=lambda: ship_balance(file_arr))
                               #command=ship_balance)
    balance_button.pack(side=tk.RIGHT, padx=10)

    def finished_cycle():
        write_to_log_file(f"Finished a cycle. Manifest {current_manifest} was written to desktop, and reminder popup to operator"
                          f" to send file was displayed.",log_file_to_write)
        upload_manifest()

    manifest_button = tk.Button(button_frame, text="Finish", font=("Helvetica", 16), command=finished_cycle)
    manifest_button.pack(side=tk.RIGHT, padx=10)

    transfer_button = tk.Button(button_frame, text="Start a transfer", font=("Helvetica", 16), command=container_transfer)
    transfer_button.pack(side=tk.LEFT, padx=10)


#Passing in an array for the ship balancing functionality
def ship_balance(arr):
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a label with the instructions
    label_text = "Commence Balancing"
    label = tk.Label(frame, text=label_text, font=("Helvetica", 18))
    label.grid(row=0, column=0, columnspan=12)

    # create a new frame for the grid
    grid_frame = tk.Frame(frame)
    grid_frame.grid(row=1, column=0, sticky="nsew")

    # create the grid
    for row in range(8):
        for col in range(12):
            cell_name = arr[row][col]
            cell = tk.Label(grid_frame, text=cell_name[:10], font=("Helvetica", 16), borderwidth=1, relief="solid")
            cell.grid(row=row, column=col, sticky="nsew")

     # configure the grid to expand and fill the remaining space
    grid_frame.columnconfigure(0, weight=1)
    for i in range(12):
        grid_frame.columnconfigure(i, weight=1)
    for i in range(9):
        grid_frame.rowconfigure(i, weight=1)

    global balanceData #balanceData originall declared dict
    balanceData = balance_ship(arr)
    #returns balanceData = (leftDictionary, rightDictionary, total_time_taken)
    #here balanceData is not a dictionary
    order_of_operations(balanceData)




def container_transfer():
    for widget in frame.winfo_children():
        widget.destroy()

    label = tk.Label(frame, text="Which type of transfer would you like to do?",
                     font=("Helvetica", 18))
    label.pack(pady=50)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    balance_button = tk.Button(button_frame, text="Unload", font=("Helvetica", 16), command=lambda: unload_operation(file_arr))
    balance_button.pack(side=tk.RIGHT, padx=10)

    transfer_button = tk.Button(button_frame, text="Load", font=("Helvetica", 16), command=load_operation)
    transfer_button.pack(side=tk.LEFT, padx=10)

def load_operation():
    for widget in frame.winfo_children():
        widget.destroy()

    global current_operation
    current_operation = "onloaded"

    # Create a label with the instructions
    label_text = "Please enter the information of the container you would like to load"
    label = tk.Label(frame, text=label_text, font=("Helvetica", 18))
    label.pack(pady=50)

    # Calculate the width of the label and use it as the width for the entry boxes
    label_width = len(label_text)  # 11 is a rough estimate of the average character width
    entry_width = label_width  # Subtract a bit to account for padding and borders

    # Create the First Name entry box
    container_weight_label = tk.Label(frame, text="Container Weight:")
    container_weight_label.pack()
    container_weight_entry = tk.Entry(frame, width=entry_width)
    container_weight_entry.pack()

    # Create the Last Name entry box
    container_name_label = tk.Label(frame, text="Container Name:")
    container_name_label.pack()
    container_name_entry = tk.Entry(frame, width=entry_width)
    container_name_entry.pack()

    def load_instruction():
        global file_arr

        new_array, best_cell = load(file_arr,container_name_entry.get(),container_weight_entry.get())
        cell_update = [r(best_cell[0]), c(best_cell[1])]

        file_arr = new_array

        for widget in frame.winfo_children():
            widget.destroy()

        # Create a label with the instructions
        label_text = "Please load the container to the indicated spot"
        label = tk.Label(frame, text=label_text, font=("Helvetica", 18))
        label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

        # create a new frame for the grid
        grid_frame = tk.Frame(frame)
        grid_frame.place(relx=0.5, rely=0.42, anchor=tk.CENTER)

        # create the grid
        for row in range(8):
            for col in range(12):
                container_name = file_arr[row][col][0]
                cell = tk.Label(grid_frame, text=container_name, font=("Helvetica", 16), borderwidth=1, relief="solid")
                cell.grid(row=row, column=col, sticky="nsew")

        # configure the grid to expand and fill the remaining space
        grid_frame.columnconfigure(0, weight=1)
        for i in range(12):
            grid_frame.columnconfigure(i, weight=1)
        for i in range(9):
            grid_frame.rowconfigure(i, weight=1)           # create the continue button
        continue_button = tk.Button(frame, text="Finished", font=("Helvetica", 16),
                                    command=balance_or_transfer)
        continue_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        # function to alternate the background color of the red cell
        def alternate_color():
            # we need a way to bring a value in
            cell = grid_frame.grid_slaves(row=cell_update[0],column=cell_update[1])[0] #Backend needs a way to find the position
            current_color = cell.cget("bg")
            new_color = "white" if current_color == "red" else "red"
            cell.config(bg=new_color)
            root.after(1000, alternate_color)  # schedule the function to run again in 1000 milliseconds (1 second)

        # start alternating the background color of the red cell
        alternate_color()

    button_frame = tk.Frame(frame)
    button_frame.pack()

    back_button = tk.Button(button_frame, text="Back", font=("Helvetica", 16), command=balance_or_transfer)
    back_button.pack(side=tk.LEFT, padx=10)

    # Create the Submit button
    submit_button = tk.Button(button_frame, text="Submit", font=("Helvetica", 16),
                              command=load_instruction)
    submit_button.pack(side=tk.RIGHT,pady=50)

def unload_operation(arr):
    for widget in frame.winfo_children():
        widget.destroy()

    global current_operation
    current_operation = "offloaded"

    # Create a label with the instructions
    label_text = "Please select the container to unload"
    label = tk.Label(frame, text=label_text, font=("Helvetica", 18))
    label.grid(row=0, column=0, columnspan=12)

    # create a new frame for the grid
    grid_frame = tk.Frame(frame)
    grid_frame.grid(row=1, column=0, sticky="nsew")

    # create the grid
    for row in range(8):
        for col in range(12):
            cell_name = arr[row][col]
            cell = tk.Label(grid_frame, text=cell_name[:10], font=("Helvetica", 16), borderwidth=1, relief="solid")
            cell.grid(row=row, column=col, sticky="nsew")
            cell.bind("<Button-1>", lambda event, name=cell_name: select_container(name))

    # configure the grid to expand and fill the remaining space
    grid_frame.columnconfigure(0, weight=1)
    for i in range(12):
        grid_frame.columnconfigure(i, weight=1)
    for i in range(9):
        grid_frame.rowconfigure(i, weight=1)

    # create the continue button
    continue_button = tk.Button(frame, text="Finished", font=("Helvetica", 16),
                                command=balance_or_transfer)
    continue_button.grid(row=11, column=0, columnspan=6, sticky="nsew")

    # Create the Submit button


def select_container(name):
    for widget in frame.winfo_children():
        widget.destroy()

    message = f"The container named {name} has been selected."
    label = tk.Label(frame, text=message, font=("Helvetica", 18))
    label.pack(pady=50)

    back_button = tk.Button(frame, text="Back", font=("Helvetica", 16),
                             command=unload_operation)
    back_button.pack()

    #Inserting functionality for unloading here assuming that we only select containers when unloading

    #actual dictionary value received from here
    moveDict = unload(file_arr, name[0])
    print(moveDict)


    generate_order = tk.Button(frame, text="Generate Order of Operations List", font=("Helvetica", 16),
                             command=lambda: order_of_operations(moveDict))
    generate_order.pack()

def order_of_operations(coords):
    for widget in frame.winfo_children():
        widget.destroy()
        # we filter out invalid moves from coordinates and put valid ones in here (tuple of dicts)

    #Here we can receive two potential values as the argument:
        # a tuple composed of the left and right dict vals (balancing)
        # an actual dict val for the movement on a single page (unloading)

    global orderOps


    validMoves = []
    operation = ""
    operations = []
    print(coords)
    # we need to implement a check to see what coords are empty
    if type(coords) == dict:
        validMoves.append(coords)
    else:
        for coord in coords[:-1]:
            if coord['name'] != '':
                validMoves.append(coord)


    for i in validMoves:
        ops = "Move" + str(i['first']) + "to" + str(i['next']) + "\n"
        operations.append(ops)

    print(operations)
    #operations = ["Move (2,1) to (2,3)", "Move (4,1) to (0,1)", "Move (X,Y) to (Z, Y)"]

    label = tk.Label(frame, text="Order of operations:", font=("Helvetica", 18))
    label.pack()

    for operation in operations:
        label = tk.Label(frame, text=operation, font=("Helvetica", 18))
        label.pack()

    coordinates = [[2, 1], [2, 3], [3, 4], [3,3], [5,2], [6,1]]

    #gotta find a way to get coordinates in here
    #coords = cycleCoords(coords)

    #Here we store the coordinates as tuples
    #dict(coordinates) = coords
    #oordinates.append()
    # here we take in back end coordinates
    generate_animation = tk.Button(frame, text="Proceed to Animation", font=("Helvetica", 16),command=lambda: animation(coords))
#                             command=lambda: animation(coordinates))

    previous_instructions = []
                             
    generate_animation.pack()


def animation(coordinates):
    for widget in frame.winfo_children():
        widget.destroy()

#

# pops a list - might need a revision
    # first_coords = coordinates.pop(0)
    # second_coords = coordinates[0]

    # we filter out invalid moves from coordinates and put valid ones in here (tuple of dicts)
    global valid_moves
    validMoves = []

    print(coordinates)
    if type(coordinates) == dict:
        validMoves.append(coordinates)
    else:# we need to implement a check to see what coords are empty
        for coord in coordinates[:-1]:
            if coord['name'] != '':
                validMoves.append(coord)


    # list of first and second coords append dictionary values of first and next
    first_coords = []
    second_coords = []
    print(validMoves)
    for i in validMoves:
        first_coords.append(i['first'])
        second_coords.append(i['next'])
    print(validMoves)



    first = first_coords.pop(len(validMoves)-1)
    second = second_coords.pop(len(validMoves)-1)


    #we should wrap this label in an if loop to check if unload or balance
    # Create a label with the instructions
    label_text = "Move" + str(first) + "to" + str(second)
    label = tk.Label(frame, text=label_text, font=("Helvetica", 18))
    label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    # create a new frame for the grid
    grid_frame = tk.Frame(frame)
    grid_frame.place(relx=0.5, rely=0.42, anchor=tk.CENTER)

    global file_arr

    # create the grid
    for row in range(8):
        for col in range(12):
                container_name = file_arr[row][col][0]
                cell = tk.Label(grid_frame, text=container_name, font=("Helvetica", 16), borderwidth=1, relief="solid")
                cell.grid(row=row, column=col, sticky="nsew")


    previous_instructions.append([first_coords])

    def go_back():
        first_coord = previous_instructions.pop()
        second_coord = previous_instructions.pop()
        animation(second_coord + first_coord + coordinates)

    def next():
        animation(coordinates)

    def finish():
        write_to_log_file(f"{current_container} is {current_operation}", log_file_to_write)
        balance_or_transfer()

    # if len(coordinates) != 1:
    #     root.bind("<space>", lambda event: animation(coordinates))
    #     # create the continue button
    #     if(previous_instructions):
    #         back_button = tk.Button(frame, text="Back", font=("Helvetica", 16),
    #                                     command= go_back)
    #         back_button.place(relx=0.44,rely=0.8, anchor=tk.CENTER)
    #     # create the continue button
    #     continue_button = tk.Button(frame, text="Next (Spacebar)", font=("Helvetica", 16),
    #                                 command= next)
    #     continue_button.place(relx=0.52,rely=0.8, anchor=tk.CENTER)
    # else:
    #     root.unbind("<space>")
    #     root.bind("<space>", lambda event: balance_or_transfer())
    #     if(previous_instructions):
    #         back_button = tk.Button(frame, text="Back", font=("Helvetica", 16),
    #                                 command= go_back)
    #         back_button.place(relx=0.44, rely=0.8, anchor=tk.CENTER)
    #
    #     # create the continue button
    #     finish_button = tk.Button(frame, text="Done (Spacebar)", font=("Helvetica", 16),
    #                                 command=finish)
    #     finish_button.place(relx=0.52,rely=0.8, anchor=tk.CENTER)


    if len(validMoves) != 1:
       # create the continue button
       continue_button = tk.Button(frame, text="Next", font=("Helvetica", 16),
                                   command= lambda: animation(coordinates))
       continue_button.place(relx=0.44, rely=0.8, anchor=tk.CENTER)
    else:
       # create the continue button
       finish_button = tk.Button(frame, text="Finished", font=("Helvetica", 16),
                                   command=balance_or_transfer)
       finish_button.place(relx=0.52,rely=0.8, anchor=tk.CENTER)

    # function to alternate the background color of the red cell
    def alternate_color():
        #lists of tuples
        #first_coords = first
        #second_coords = next
        cell1 = grid_frame.grid_slaves(row=8 - first[0], column=first[1]-1)[0]  # Backend needs a way to find the position
        cell2 = grid_frame.grid_slaves(row=8 - second[0],column=second[1]-1)[0]
        old_color = cell1.cget("bg")
        new_color = "white" if old_color == "red" else "red"
        cell1.config(bg=new_color)
        cell2.config(bg=old_color)
        root.after(1000, alternate_color)  # schedule the function to run again in 1000 milliseconds (1 second)

    # start alternating the background color of the red cell
    alternate_color()

def input_name():

    def submit_name():
        global full_name
        full_name = full_name_entry.get()
        print("Name:", full_name)
        if log_file_to_write != "":
            write_to_log_file(f"{full_name} signs in", log_file_to_write)
        username_prompt.destroy() # Close the prompt window after submission

    if log_file_to_write != "" :
        write_to_log_file(f"{full_name} signs out", log_file_to_write)

    username_prompt = tk.Tk()

    # Calculate the center of the screen
    screen_width = username_prompt.winfo_screenwidth()
    screen_height = username_prompt.winfo_screenheight()
    x = int((screen_width / 2) - (300 / 2))
    y = int((screen_height / 2) - (150 / 2))

    # Set the position of the window to the center of the screen
    username_prompt.geometry("+{}+{}".format(x, y))
    username_prompt.title("Enter Full Name")

    # Create a label with the instructions
    label_text = "Please enter your full name in the box below"
    label = tk.Label(username_prompt, text=label_text, font=("Helvetica", 18))
    label.pack(pady=50)

    # Calculate the width of the label and use it as the width for the entry boxes
    label_width = len(label_text)  # 11 is a rough estimate of the average character width
    entry_width = label_width  # Subtract a bit to account for padding and borders

    # Create the First Name entry box
    first_name_label = tk.Label(username_prompt, text="Full Name:")
    first_name_label.pack()
    full_name_entry = tk.Entry(username_prompt, width=entry_width)
    full_name_entry.insert(0,"Firstname Lastname")
    full_name_entry.bind("<FocusIn>", lambda args:full_name_entry.delete('0','end'))
    full_name_entry.pack()

    # Create the Submit button
    submit_button = tk.Button(username_prompt, text="Submit", font=("Helvetica", 16), command=submit_name)
    submit_button.pack(pady=50)

def add_comment():
    def submit_comment():
        comment = comment_entry.get("1.0",tk.END)
        write_to_log_file(comment,log_file_to_write)
        comment_prompt.destroy() # Close the prompt window after submission

    comment_prompt = tk.Tk()
    comment_prompt.geometry('300x150')
    comment_prompt.title("Add Comment")

    comment_label = tk.Label(comment_prompt, text="Please enter a comment:")
    comment_label.pack(side="top")

    comment_entry = tk.Text(comment_prompt, height=5 ,width=50)
    comment_entry.pack(side="top")

    submit_button = tk.Button(comment_prompt, text="Submit", command=submit_comment)
    submit_button.pack(side="bottom")

def main():
    program_start()
    root.mainloop()

if __name__ == "__main__":

    #creating intial file
    file_name = "KeoghLongBeach.txt" #global file_name that should be converted into array
    file_arr = []
    operation = "string"
    balanceData = {
        'coord_list': [],
        'name': '',
        'first': (),
        'next': (),
        'time_taken': 0,
        'time_to_move': 0
    }
    orderOps = []
    validMoves = []

    root = tk.Tk()
    root.geometry(
        '{}x{}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))  # Set window dimensions to full screen
    root.title("Container Application")

    # Create a frame to hold all of the content
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    # Create a menu bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # Create an "Actions" dropdown menu
    actions_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Actions", menu=actions_menu)
    actions_menu.add_command(label="Add comment (CTRL + U)", command=add_comment)
    actions_menu.add_command(label="Sign In (CTRL + S)", command=input_name)

    root.bind("<Control-s>", lambda event: input_name())
    root.bind("<Control-u>", lambda event: add_comment())
    main()
