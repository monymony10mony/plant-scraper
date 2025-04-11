import requests
from bs4 import BeautifulSoup
import pandas as pd

# Wikipedia page with plant distribution data
URL = "https://en.wikipedia.org/wiki/List_of_plants_of_the_American_Deserts"

# Request the page content
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve the page")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the table that contains plant data
table = soup.find("table", {"class": "wikitable"})

# Extract table rows
data = []
if table:
    rows = table.find_all("tr")[1:]  # Skip header row
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2:  # Ensure there are enough columns
            plant_name = cols[0].text.strip()
            distribution = cols[1].text.strip()
            data.append([plant_name, distribution])

# Save the data to a CSV file
df = pd.DataFrame(data, columns=["Plant Name", "Distribution"])
df.to_csv("plants_data.csv", index=False)

print("✅ Data successfully scraped and saved to plants_data.csv!")
