from tkinter import *
from tkinter import simpledialog
from PIL import Image, ImageTk

def create_window():
    new_window = Tk()
    two_window = Tk()

    # Create buttons with custom size
    Button(new_window, text="Create new window", width=15, height=2).pack()

    # Load and display an image in two_window
    image = Image.open("aapl.png")  # Replace with the path to your image
    photo = ImageTk.PhotoImage(image)
    image_label = Label(two_window, image=photo)
    image_label.photo = photo  # To prevent the image from being garbage collected
    image_label.pack()

    new_window.geometry("400x300")
    two_window.geometry("400x300")

    new_window.mainloop()
    two_window.mainloop()

# Display the input dialog box
user_input = simpledialog.askstring("Input", "Company Ticker:")

# Check if the user clicked "OK" and entered a value
if user_input is not None and user_input.strip() != "":
    create_window()
else:
    print("User canceled the input or entered nothing.")