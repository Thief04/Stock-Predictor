import tkinter as tk
from tkinter import simpledialog

def create_window():
    new_window = tk.Tk()
    canvas_window = tk.Tk()

    # Create buttons with custom size
    tk.Button(canvas_window, text="Income Statement", width=15, height=2).pack()

    # Load and display an image in canvas_window
    image = tk.PhotoImage(file="knowledge_graph_logo.png")  # Replace with your image file path
    image_label = tk.Label(new_window, image=image)
    image_label.image = image  # To prevent the image from being garbage collected
    image_label.pack()

    new_window.geometry("400x300")
    canvas_window.geometry("400x300")

    new_window.mainloop()
    canvas_window.mainloop()

# Display the input dialog box
user_input = simpledialog.askstring("Input", "Company Ticker:")

if user_input is not None and user_input.strip() != "":
    create_window()
else:
    print("User canceled the input or entered nothing.")



