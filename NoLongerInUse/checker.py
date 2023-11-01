#This code is no longer in use, it is here from when I was teaching myself HTTP requests.


import requests
import string
from bs4 import BeautifulSoup

# Make an HTTP request to the website
valid_tickers = []  # Initialize an empty list to store valid tickers

uppercase_alphabet = string.ascii_uppercase
for letter in uppercase_alphabet:
    url = "https://eoddata.com/stocklist/NYSE/" + letter + ".htm"  # Replace with the actual URL
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <a> elements with the specified format
        elements = soup.find_all('a', href=True, title=True, string=True)

        # Extract valid tickers from elements where 'GHAUK' is a placeholder
        valid_tickers.extend([element.text.strip() for element in elements if 'NYSE,' in element['title']])

    else:
        print(f"Failed to fetch data from {url}")

# Get user input
user_input = input("Enter a company ticker on the NYSE: ").strip().upper()

# Check if the input is valid
if user_input in valid_tickers:
    print(f"{user_input} is a valid NYSE ticker.")
else:
    print(f"{user_input} is not a valid NYSE ticker.")
    print("Valid Tickers:", valid_tickers)

