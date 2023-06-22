"""
Data collection and analysis: This program develops a system that collects and analyzes data on food 
production, distribution, and consumption in the DRC. This system uses Python to scrape data from 
various sources, such as government databases, news articles, and social media, and then use data analysis 
techniques to identify patterns and trends.
"""
"""
This program uses the requests library to send HTTP requests to the URLs that contain the food production, 
distribution, and consumption data for the DRC. It then uses BeautifulSoup to parse the HTML content of the 
pages and extract the relevant data.

The program then converts the data to pandas dataframes and merges them into a single dataframe. 

Finally, it performs some data analysis on the merged dataframe, calculating the percentage of food that is 
produced, distributed, and consumed each year. The results are printed to the console.

This is just a basic example of how you could collect and analyze data on food production, distribution, and 
consumption in the DRC using Python. Depending on your specific goals, you may need to modify the program to suit your needs.
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URLs for data sources
food_production_url =  'https://agriculture.canada.ca/en/sector/animal-industry/red-meat-livestock-market-information/industry-profile'   #'http://www.stat-gouv.cd/indicateur.php?ico=prd1&idd=1'
food_distribution_url = 'https://agriculture.canada.ca/en/news-agriculture-and-agri-food-canada/improve-food-conservation-canadas-distribution-chain' #'http://www.stat-gouv.cd/indicateur.php?ico=con1&idd=1'
food_consumption_url = 'https://agriculture.canada.ca/en/international-trade/market-intelligence/reports/sector-trend-analysis-fish-and-seafood-trends-philippines'#'http://www.stat-gouv.cd/indicateur.php?ico=con1&idd=3'

# Scrape the data from the URLs using BeautifulSoup
production_page = requests.get(food_production_url)
production_soup = BeautifulSoup(production_page.content, 'html.parser')

distribution_page = requests.get(food_distribution_url)
distribution_soup = BeautifulSoup(distribution_page.content, 'html.parser')

consumption_page = requests.get(food_consumption_url)
consumption_soup = BeautifulSoup(consumption_page.content, 'html.parser')

# Extract the relevant data from the HTML
production_data = []
for row in production_soup.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) == 2:
        production_data.append([columns[0].text.strip(), columns[1].text.strip()])

distribution_data = []
for row in distribution_soup.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) == 2:
        distribution_data.append([columns[0].text.strip(), columns[1].text.strip()])

consumption_data = []
for row in consumption_soup.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) == 2:
        consumption_data.append([columns[0].text.strip(), columns[1].text.strip()])

# Convert the data to pandas dataframes
production_df = pd.DataFrame(production_data, columns=['Year', 'Production'])
distribution_df = pd.DataFrame(distribution_data, columns=['Year', 'Distribution'])
consumption_df = pd.DataFrame(consumption_data, columns=['Year', 'Consumption'])

# Merge the dataframes into a single dataframe
merged_df = pd.merge(production_df, distribution_df, on='Year')
merged_df = pd.merge(merged_df, consumption_df, on='Year')

# Perform data analysis on the merged dataframe
# For example, calculate the percentage of food that is produced, distributed, and consumed each year
merged_df['Production %'] = merged_df['Production'] / merged_df['Consumption'] * 100
merged_df['Distribution %'] = merged_df['Distribution'] / merged_df['Consumption'] * 100

# Print the results
print(merged_df)