import csv
import requests
from bs4 import BeautifulSoup

csvfile = open('patrol.csv', 'a')
patrol_writer = csv.writer(csvfile)

########## GET HTML ##########

url = 'https://www.mshp.dps.missouri.gov/HP68/SearchAction?searchDate=10/17/2015'
html = requests.get(url).content

########## MAKE SOUP ##########

soup = BeautifulSoup(html, 'html.parser')

########## DO SCRAPE ##########

table = soup.find('table', {'class': 'accidentOutput'})

rows = table.find_all('tr')

for row in rows:

    tds = row.find_all('td')

    output = []
    for td in tds:
        output.append(td.text.strip())

    patrol_writer.writerow(output)