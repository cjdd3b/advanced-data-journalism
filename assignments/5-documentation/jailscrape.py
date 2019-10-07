import urllib2, csv
from bs4 import BeautifulSoup

outfile = open('jaildata.csv', 'w')
writer = csv.writer(outfile)

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

tbody = soup.find('tbody', {'class': 'stripe'})

rows = tbody.find_all('tr')

for row in rows:

    cells = row.find_all('td')

    data = []
    for cell in cells:
        data.append(cell.text.encode('utf-8'))

    writer.writerow(data)
