from tkinter import *
from tkinter import simpledialog

def create_window():
    new_window = Tk()
    two_window = Tk()
    
    Button(new_window,text="create new window").pack()
    Button(two_window,text="create new window").pack()

    new_window.mainloop()
    two_window.mainloop()

# Display the input dialog box
user_input = simpledialog.askstring("Input", "Company Ticker:")



# Check if the user clicked "OK" and entered a value
if user_input is not None and user_input.strip() != "":
    create_window()
else:
    print("User cancelled the input or entered nothing.")

