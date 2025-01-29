import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/raw-fruits-poster-text-version-accessible-version'  # Replace with the actual URL

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.content, 'html.parser')

# Find the first table on the webpage
table = soup.find('table')

# Dictionary to store fruit names and their corresponding calories
data = {}

# Iterate over each row in the table (excluding the header)
for row in table.find_all('tr')[1:]:
    # Find the table header and data cells in the row
    th = row.find('th')
    td = row.find('td')

    # If both cells exist
    if th and td:
        # Extract the text from the table header cell
        text = th.get_text(separator=' ', strip=True)
        words = text.split()

        # Extract the fruit name
        if len(words) > 1 and words[1].isalpha():
            fruit = ' '.join(words[:2]).casefold()
        else:
            fruit = words[0].casefold()

        # Extract the calories from the data cell
        calories = int(td.get_text())
        # Store the fruit name and calories in the dictionary
        data[fruit] = calories

def main():
    # Get the user's query
    query_fruit = input("Item: ").casefold()

    if query_fruit in data:
        print(f"Calories: {data[query_fruit]}")

main()
