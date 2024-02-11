import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

html = requests.get(url)

soup = BeautifulSoup(html.content, "html.parser")

result = soup.find("table", class_="wikitable sortable")

# Extract column titles
title_elements = result.find_all("th")
column_titles = [title.text.strip() for title in title_elements]

dataf = pd.DataFrame(columns=column_titles)

# Extract data for each row
rows = result.find_all("tr")[1:]  # Skip the header row
for row in rows:
    column_data = row.find_all("td")
    data_clm = [data.text.strip() for data in column_data]
    length = len(dataf)
    dataf.loc[length] = data_clm


# Converting the Data File into a CSV file. 
# dataf.to_csv(r"C:\Users\Jaime Manzueta\OneDrive\Desktop\pro.py/companies.csv", index= False)


