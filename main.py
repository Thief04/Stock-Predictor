import tkinter as tk
from tkinter import simpledialog
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
import yfinance as yf
import pandas as pd
from selenium import webdriver
import time

def format_income_statement(income_stmt):
    # Format the income statement by adding commas to large numbers
    formatted_income_stmt = income_stmt.applymap(lambda x: f'{x:,.0f}' if isinstance(x, (int, float)) else x)
    return formatted_income_stmt

def income_statement(ticker):
    income_window = tk.Toplevel()
    income_window.title(ticker)

    # Fetch income statement data using yfinance
    stock = yf.Ticker(ticker)
    income_stmt = stock.financials

    # Format the income statement
    formatted_income_stmt = format_income_statement(income_stmt)

    # Create a Text widget to display the formatted income statement
    income_text = tk.Text(income_window)
    income_text.pack(expand=True, fill='both')

    # Insert the formatted income statement data into the Text widget
    income_text.insert('1.0', formatted_income_stmt.to_string())
    income_window.geometry("1200x1000")
    income_window.mainloop()

def create_window(ticker):
    new_window = tk.Toplevel()
    canvas_window = tk.Toplevel()

    # Create buttons with custom size
    tk.Button(canvas_window, text="Income Statement for " + ticker, command=lambda t=ticker: income_statement(t), width=30, height=5).pack()

    # Initialize the WebDriver
    driver = webdriver.Chrome()  # You can use a different WebDriver here (e.g., Firefox, Edge, etc.)

    # Open a webpage
    driver.get("https://ca.finance.yahoo.com/chart/" + ticker + "#eyJpbnRlcnZhbCI6ImRheSIsInBlcmlvZGljaXR5IjoxLCJ0aW1lVW5pdCI6bnVsbCwiY2FuZGxlV2lkdGgiOjgsImZsaXBwZWQiOmZhbHNlLCJ2b2x1bWVVbmRlcmxheSI6dHJ1ZSwiYWRqIjp0cnVlLCJjcm9zc2hhaXIiOnRydWUsImNoYXJ0VHlwZSI6ImxpbmUiLCJleHRlbmRlZCI6ZmFsc2UsIm1hcmtldFNlc3Npb25zIjp7fSwiYWdncmVnYXRpb25UeXBlIjoib2hsYyIsImNoYXJ0U2NhbGUiOiJsaW5lYXIiLCJwYW5lbHMiOnsiY2hhcnQiOnsicGVyY2VudCI6MSwiZGlzcGxheSI6IkFBUEwiLCJjaGFydE5hbWUiOiJjaGFydCIsImluZGV4IjowLCJ5QXhpcyI6eyJuYW1lIjoiY2hhcnQiLCJwb3NpdGlvbiI6bnVsbH0sInlheGlzTEhTIjpbXSwieWF4aXNSSFMiOlsiY2hhcnQiLCLigIx2b2wgdW5kcuKAjCJdfX0sInNldFNwYW4iOnt9LCJsaW5lV2lkdGgiOjIsInN0cmlwZWRCYWNrZ3JvdW5kIjp0cnVlLCJldmVudHMiOnRydWUsImNvbG9yIjoiIzAwODFmMiIsInN0cmlwZWRCYWNrZ3JvdWQiOnRydWUsImV2ZW50TWFwIjp7ImNvcnBvcmF0ZSI6eyJkaXZzIjp0cnVlLCJzcGxpdHMiOnRydWV9LCJzaWdEZXYiOnt9fSwic3ltYm9scyI6W3sic3ltYm9sIjoiQUFQTCIsInN5bWJvbE9iamVjdCI6eyJzeW1ib2wiOiJBQVBMIiwicXVvdGVUeXBlIjoiRVFVSVRZIiwiZXhjaGFuZ2VUaW1lWm9uZSI6IkFtZXJpY2EvTmV3X1lvcmsifSwicGVyaW9kaWNpdHkiOjEsImludGVydmFsIjoiZGF5IiwidGltZVVuaXQiOm51bGwsInNldFNwYW4iOnt9fV0sInN0dWRpZXMiOnsi4oCMdm9sIHVuZHLigIwiOnsidHlwZSI6InZvbCB1bmRyIiwiaW5wdXRzIjp7ImlkIjoi4oCMdm9sIHVuZHLigIwiLCJkaXNwbGF5Ijoi4oCMdm9sIHVuZHLigIwifSwib3V0cHV0cyI6eyJVcCBWb2x1bWUiOiIjMDBiMDYxIiwiRG93biBWb2x1bWUiOiIjZmYzMzNhIn0sInBhbmVsIjoiY2hhcnQiLCJwYXJhbWV0ZXJzIjp7IndpZHRoRmFjdG9yIjowLjQ1LCJjaGFydE5hbWUiOiJjaGFydCIsInBhbmVsTmFtZSI6ImNoYXJ0In19fX0-")  # Replace with the URL of the webpage you want to screenshot
    time.sleep(1)
    
    # Take a screenshot
    driver.save_screenshot("screenshot.png")  # Provide the desired file name for the screenshot
    image = Image.open("screenshot.png")
    driver.quit()

    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(new_window, image = photo)
    image_label.pack()

    new_window.geometry("1600x1200")
    canvas_window.geometry("400x300")

    new_window.mainloop()
    canvas_window.mainloop()

def main_function():
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
        create_window(user_input)

    # Create a button to submit the input
    submit_button = tk.Button(root, text="Submit", command=handle_button_click)
    submit_button.pack()

    root.mainloop()

main_function()




