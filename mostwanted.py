# Import libraries
import csv
import requests
from bs4 import BeautifulSoup

# Collect first page of fugitives list
page = requests.get('https://www.fbi.gov/wanted/topten')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Create a file to write to and add header
f = csv.writer(open('ten-most-wanted.csv','w'))
f.writerow(['Name', ])

# Pull all text from the div that name is under
fugitive_name_list = soup.find(class_="query-results pat-pager")

# Narrow down to all instances of <a> tag under div
fugitive_name_list_items = fugitive_name_list.find_all('a')

# Create for loop to print out all fugitives' names
for fugitive_name in fugitive_name_list_items:
    names = fugitive_name.contents[0]

    # Add names under header
    f.writerow([names])
