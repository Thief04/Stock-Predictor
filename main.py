import tkinter as tk
from tkinter import simpledialog
import requests
import string
from bs4 import BeautifulSoup
from PIL import Image, ImageTk

def income_statement(ticker):
    income_window = tk.Toplevel()
    income_window.title(ticker)

    # Create a Label widget to display the ticker text
    ticker_label = tk.Label(income_window, text=ticker)
    ticker_label.pack(expand=True)  # This will center the label in the window

    # You can add more widgets and functionality here if needed

    income_window.geometry("200x100")

    income_window.mainloop()


def create_window(ticker):
    new_window = tk.Toplevel()
    canvas_window = tk.Toplevel()

    # Create buttons with custom size
    tk.Button(canvas_window, text="Income Statement for " + ticker, command=lambda t=ticker: income_statement(t), width=30, height=5).pack()


    # Load and display an image in canvas_window using Pillow
    image = Image.open("knowledge_graph_logo.png")
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(new_window, image = photo)
    image_label.pack()

    new_window.geometry("400x300")
    canvas_window.geometry("400x300")

    new_window.mainloop()
    canvas_window.mainloop()



def main_function():
    # Make an HTTP request to the website and fetch valid tickers
    valid_tickers = []

    uppercase_alphabet = string.ascii_uppercase
    for letter in uppercase_alphabet:
        url = "https://eoddata.com/stocklist/NYSE/" + letter + ".htm"
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all <a> elements with the specified format
            elements = soup.find_all('a', href=True, title=True, string=True)

            # Extract valid tickers from elements where 'NYSE,' is in the title
            valid_tickers.extend([element.text.strip() for element in elements if 'NYSE,' in element['title']])

        else:
            print(f"Failed to fetch data from {url}")

    # Create the main application window
    root = tk.Tk()
    root.geometry("400x100")
    root.title("Input Dialog")

    # Create an Entry widget for user input
    entry = tk.Entry(root)
    entry.pack()

    # Function to handle button click and validate input
    def handle_button_click():
        user_input = entry.get().strip().upper()
        if user_input != "" and user_input in valid_tickers:
            create_window(user_input)
        else:
            print(f"{user_input} is not a valid NYSE ticker.")

    # Create a button to submit the input
    submit_button = tk.Button(root, text="Submit", command=handle_button_click)
    submit_button.pack()

    root.mainloop()


user_input = input("here: ").upper()
create_window(user_input)
