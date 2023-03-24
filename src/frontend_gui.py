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
        continue_button.pack(side="top", anchor="center",pady=50)

#frame 1
def start_a_new_log_file_prompt():

    # Clear the existing widgets in the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Add a label to the frame with the welcome message
    welcome_label = tk.Label(frame, text="Welcome!", font=("Helvetica", 18))
    welcome_label.pack(pady=50)

    # Add new log file prompt to the frame
    prompt_label = tk.Label(frame, text="Would you like to start a new log file?", font=("Helvetica", 16))
    prompt_label.pack(pady=50)

    # Add yes and no buttons to the frame
    button_frame = tk.Frame(frame)
    button_frame.pack()

    no_button = tk.Button(button_frame, text="No", font=("Helvetica", 16), command=load_existing_log_file)
    no_button.pack(side=tk.RIGHT, padx=10)

    yes_button = tk.Button(button_frame, text="Yes", font=("Helvetica", 16), command=create_new_log_file)
    yes_button.pack(side=tk.LEFT, padx=10)

# Define functions for handling button clicks
#Frame 3
def create_new_log_file():
    # Code to create a new log file
    for widget in frame.winfo_children():
        widget.destroy()

    append_year_label = tk.Label(frame, text="Creating default log file named 'KeoghLongBeach.txt'."
                                         "\nWould you like to append the current year?"
                                         f"\nCurrent Year: {current_year} ", font=("Helvetica", 18))
    append_year_label.pack(pady=50)

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

    confirm_label = tk.Label(frame, text=f"Created default log file 'KeoghLongBeach{current_year}.txt'.", font=("Helvetica", 18))
    confirm_label.pack(pady=50)

    # Continue
    continue_button = tk.Button(frame, text="Continue", font=("Helvetica", 16), command=upload_manfiest)
    continue_button.pack(pady=50)

def no_append_year():
    for widget in frame.winfo_children():
        widget.destroy()

    confirm_label = tk.Label(frame, text=f"Created default log file 'KeoghLongBeach.txt'.",
                             font=("Helvetica", 18))
    confirm_label.pack(pady=50)

    # Continue
    continue_button = tk.Button(frame, text="Continue", font=("Helvetica", 16), command=upload_manfiest)
    continue_button.pack(pady=50)

def resume():
    for widget in frame.winfo_children():
        widget.destroy()

    welcome_label = tk.Label(frame, text="This application has detected that the previous executation has been interrupted"
                                         "\nWould you like to resume the program?",
                             font=("Helvetica", 18))
    welcome_label.pack(pady=50)

    # Continue
    continue_button = tk.Button(frame, text="Continue", font=("Helvetica", 16), command=program_start)
    continue_button.pack(pady=50)

#frame 2
def load_existing_log_file():
    # Code to load an existing log file
    for widget in frame.winfo_children():
        widget.destroy()

    default_log_label = tk.Label(frame, text=f"Using default log file 'KeoghLongBeach{current_year}.txt'.",
                             font=("Helvetica", 18))
    default_log_label.pack(pady=50)

    # Put the buttons in a new frame
    button_frame = tk.Frame(frame)
    button_frame.pack()

    back_button = tk.Button(button_frame, text="Back", font=("Helvetica", 16), command=start_a_new_log_file_prompt)
    back_button.pack(side=tk.LEFT, padx=10)

    continue_button = tk.Button(button_frame, text="Continue", font=("Helvetica", 16), command=upload_manfiest)
    continue_button.pack(side=tk.LEFT, padx=10, pady=50)

def shorten_file(filename):
    file = os.path.split(filename)[1]
    return file

#takes file input
#frame 4
def upload_manfiest():
    for widget in frame.winfo_children():
        widget.destroy()

    upload_label = tk.Label(frame, text="Please upload a Manifest file",
                             font=("Helvetica", 18))
    upload_label.pack(pady=50)

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
            file_arr = manifest_init(file_path)  # txt file passed into manifest_init to be transformed into arr

    continue_button = tk.Button(frame, text="Continue", font=("Helvetica", 16), command=balance_or_transfer)
    button = tk.Button(frame, text="Select File", command=browse_file)
    button.pack(pady=50)

#Here we want to call manifest_init() to translate it
def balance_or_transfer():
    for widget in frame.winfo_children():
        widget.destroy()

    root.unbind("<space>")

    operation_label = tk.Label(frame, text="Please select an operation",
                     font=("Helvetica", 18))
    operation_label.pack(pady=50)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    balance_button = tk.Button(button_frame, text="Balance the ship", font=("Helvetica", 16), command=ship_balance)
    balance_button.pack(side=tk.RIGHT, padx=10)

    manifest_button = tk.Button(button_frame, text="Upload another manifest file", font=("Helvetica", 16), command=upload_manfiest)
    manifest_button.pack(side=tk.LEFT, padx=10)

    transfer_button = tk.Button(button_frame, text="Start a transfer", font=("Helvetica", 16), command=container_transfer)
    transfer_button.pack(side=tk.LEFT, padx=10)


#Passing in an array for the ship balancing functionality
def ship_balance(arr):
    balance_ship(file_arr)

def container_transfer():
    for widget in frame.winfo_children():
        widget.destroy()

    transfer_label = tk.Label(frame, text="Which type of transfer would you like to do?",
                     font=("Helvetica", 18))
    transfer_label.pack(pady=50)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    balance_button = tk.Button(button_frame, text="Unload", font=("Helvetica", 16), command=unload_operation)
    balance_button.pack(side=tk.RIGHT, padx=10)

    transfer_button = tk.Button(button_frame, text="Load", font=("Helvetica", 16),
                                command=load_operation)
    transfer_button.pack(side=tk.LEFT, padx=10)

def load_operation():
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a label with the instructions
    label_text = "Please enter the information of the container you would like to load"
    container_info_label = tk.Label(frame, text=label_text, font=("Helvetica", 18))
    container_info_label.pack(pady=50)

    # Calculate the width of the label and use it as the width for the entry boxes
    label_width = len(label_text)  # 11 is a rough estimate of the average character width
    entry_width = label_width  # Subtract a bit to account for padding and borders

    # Create the First Name entry box
    first_name_label = tk.Label(frame, text="Container Weight:")
    first_name_label.pack()
    first_name_entry = tk.Entry(frame, width=entry_width)
    first_name_entry.pack()

    # Create the Last Name entry box
    last_name_label = tk.Label(frame, text="Container Name:")
    last_name_label.pack()
    last_name_entry = tk.Entry(frame, width=entry_width)
    last_name_entry.pack()

    def load_instruction():
        for widget in frame.winfo_children():
            widget.destroy()

        # Create a label with the instructions
        label_text = "Please load the container to the indicated spot"
        load_container_label = tk.Label(frame, text=label_text, font=("Helvetica", 18))
        load_container_label.grid(row=0, column=0, columnspan=12, padx=60)

        # create a new frame for the grid
        grid_frame = tk.Frame(frame)
        grid_frame.grid(row=1, column=0, sticky="nsew", padx=60)

        # create the grid
        for row in range(8):
            for col in range(12):
                if(row == 0 and col == 0): #This will be changed to if
                    cell = tk.Label(grid_frame, font=("Helvetica", 16), borderwidth=1, relief="solid", bg='red')
                    cell.grid(row=row, column=col, sticky="nsew")
                else:
                    cell_name = f"Walmart Container"
                    cell_weight = f"{row}{col}"
                    cell = tk.Label(grid_frame, text=cell_name[:17] + "... " + cell_weight, font=("Helvetica", 16),
                                    borderwidth=1, relief="solid", wraplength=135)
                    cell.grid(row=row, column=col, sticky="nsew")

        # configure the grid to expand and fill the remaining space
        grid_frame.columnconfigure(0, weight=1)
        for i in range(12):
            grid_frame.columnconfigure(i, weight=1)
        for i in range(9):
            grid_frame.rowconfigure(i, weight=1)

            # create the continue button
        continue_button = tk.Button(frame, text="Finished", font=("Helvetica", 16),
                                    command=balance_or_transfer)
        continue_button.grid(row=11, column=0, columnspan=12, sticky="nsew", padx=50)

        # function to alternate the background color of the red cell
        def alternate_color():
            cell = grid_frame.grid_slaves(row=0,column=0)[0] #Backend needs a way to find the position
            current_color = cell.cget("bg")
            new_color = "white" if current_color == "red" else "red"
            cell.config(bg=new_color)
            root.after(1000, alternate_color)  # schedule the function to run again in 1000 milliseconds (1 second)

        # start alternating the background color of the red cell
        alternate_color()

    # Create the Submit button
    submit_button = tk.Button(frame, text="Submit", font=("Helvetica", 16),
                              command=load_instruction)
    submit_button.pack(pady=50)

def unload_operation():
    for widget in frame.winfo_children():
        widget.destroy()

    def select_container(name):
        label.configure(text=f"Unload {name}")
        continue_button.place(relx=0.65, rely=0.8, anchor=tk.CENTER)

    #    create a new frame for the grid
    grid_frame = tk.Frame(frame)
    grid_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    # create the grid
    for row in range(8):
        for col in range(12):
            cell_name = f"Walmart Container"
            cell_weight = f"{row}{col}"
            cell = tk.Label(grid_frame, text=cell_name[:17] + "... " + cell_weight, font=("Helvetica", 16), borderwidth=1, relief="solid", wraplength=135)
            cell.grid(row=row, column=col, sticky="nsew")
            cell.bind("<Button-1>", lambda event, name=cell_name: select_container(name))


    label_text = "Please select a container to unload"
    label = tk.Label(frame, text=label_text, font=("Helvetica", 16))
    label.place(relx=0.5,rely=0.8, anchor=tk.CENTER)

    # create the continue button
    continue_button = tk.Button(frame, text="Continue", font=("Helvetica", 16),
                                command=order_of_operations)


    # Create the Submit button



def order_of_operations():
    for widget in frame.winfo_children():
        widget.destroy()
    operations = ["Move (2,1) to (2,3)", "Move (4,1) to (0,1)", "Move (X,Y) to (Z, Y)"]

    label = tk.Label(frame, text="Order of operations:", font=("Helvetica", 18))
    label.pack()

    for operation in operations:
        label = tk.Label(frame, text=operation, font=("Helvetica", 18))
        label.pack()

    coordinates = [[2, 1], [2, 3], [3, 4], [3,3], [5,2], [6,1]]

    generate_animation = tk.Button(frame, text="Proceed to Animation", font=("Helvetica", 16),
                             command=lambda: animation(coordinates))

    previous_instructions = []

    generate_animation.pack()

def animation(coordinates):

    for widget in frame.winfo_children():
        widget.destroy()
        # Create a label with the instructions

    first_coords = coordinates.pop(0)
    second_coords = coordinates[0]

    label = tk.Label(frame, text=f"Move ({first_coords[0]},{first_coords[1]}) to ({second_coords[0]},{second_coords[1]})", font=("Helvetica", 18))
    label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    # create a new frame for the grid
    grid_frame = tk.Frame(frame)
    grid_frame.place(relx=0.5, rely=0.42, anchor=tk.CENTER)

    # create the grid
    for row in range(8):
        for col in range(12):
                cell_name = f"Walmart Container"
                cell_weight = f"{row}{col}"
                cell = tk.Label(grid_frame, text=cell_name[:17] + "... " + cell_weight, font=("Helvetica", 16),
                                borderwidth=1, relief="solid", wraplength=135)
                cell.grid(row=row, column=col, sticky="nsew")


    previous_instructions.append([first_coords])

    def go_back():
        first_coord = previous_instructions.pop()
        second_coord = previous_instructions.pop()
        animation(second_coord + first_coord + coordinates)

    def next():
        animation(coordinates)

    if len(coordinates) != 1:
        root.bind("<space>", lambda event: animation(coordinates))
        # create the continue button
        if(previous_instructions):
            back_button = tk.Button(frame, text="Back", font=("Helvetica", 16),
                                        command= go_back)
            back_button.place(relx=0.44,rely=0.8, anchor=tk.CENTER)
        # create the continue button
        continue_button = tk.Button(frame, text="Next (Spacebar)", font=("Helvetica", 16),
                                    command= next)
        continue_button.place(relx=0.52,rely=0.8, anchor=tk.CENTER)
    else:
        root.unbind("<space>")
        root.bind("<space>", lambda event: balance_or_transfer())
        if(previous_instructions):
            back_button = tk.Button(frame, text="Back", font=("Helvetica", 16),
                                    command= go_back)
            back_button.place(relx=0.44, rely=0.8, anchor=tk.CENTER)

        # create the continue button
        finish_button = tk.Button(frame, text="Done (Spacebar)", font=("Helvetica", 16),
                                    command=balance_or_transfer)
        finish_button.place(relx=0.52,rely=0.8, anchor=tk.CENTER)

    # function to alternate the background color of the red cell
    def alternate_color():
        cell1 = grid_frame.grid_slaves(row=first_coords[0], column=first_coords[1])[0]  # Backend needs a way to find the position
        cell2 = grid_frame.grid_slaves(row=second_coords[0],column=second_coords[1])[0]
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
        username_prompt.destroy() # Close the prompt window after submission

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
        print("Comment:", comment)
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
    order_of_operations()
    root.mainloop()

if __name__ == "__main__":

    #creating intial file
    file_name = "KeoghLongBeach.txt" #global file_name that should be converted into array
    file_arr = []
    root = tk.Tk()
    root.geometry(
        '{}x{}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))  # Set window dimensions to full screen
    root.title("Container Application")

    # Create a frame to hold all of the content
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

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