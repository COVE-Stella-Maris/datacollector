from bs4 import BeautifulSoup
import requests
import csv
import lxml

title = []
rowInfo = []
dataHeaders = []

page = requests.get('https://www.ndbc.noaa.gov/sar.php?station=44258')
soup = BeautifulSoup(page.text, 'lxml')


title.append(soup.title.string)

numRows = soup.find_all('tr')

for th in soup.find_all('th'):
    dataHeaders.append(th.text)
print(dataHeaders)

for td in numRows:
    if td.get('bgcolor') == "#f0f8fe" or td.get('bgcolor') == "#fffff0":
        rowInfo.append(td.text)

print(rowInfo)

with open('collected.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(title)
    w.writerow(dataHeaders)
    f.close()