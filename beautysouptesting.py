from bs4 import BeautifulSoup
import requests
import csv
import psycopg2

title = []
rowInfo = []
dataHeaders = []

# Request to Page
page = requests.get('https://www.ndbc.noaa.gov/sar.php?station=44258&list=all')
soup = BeautifulSoup(page.text, 'lxml')

# Grabbing Page Title
title.append(soup.title.string)

# Grabbing Data Headers
numRows = soup.find_all('tr')
for th in soup.find_all('th'):
    dataHeaders.append(th.text.strip())
print(dataHeaders)

# Grabbing Data from Table
for td in numRows:
    if td.get('bgcolor') == "#f0f8fe" or td.get('bgcolor') == "#fffff0":
        rowInfo.append(td.text)
print(rowInfo)

# CSV file Testing
with open('collected.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(title)
    w.writerow(dataHeaders)
    f.close()

# Connecting to Database
conn = psycopg2.connect(host="localhost", database="DataScrapingDB", user="Emerson", password="postgres")
curr = conn.cursor()
curr.execute("delete from testerdb where id>=0")

# Populating Databasea
x = 0
while x < len(rowInfo):
    curr.execute("insert into testerdb (id, data) values (%s, %s)", (x, rowInfo[x]))
    x = x + 1
var = curr.execute("select * from testerdb")
rows = curr.fetchall()
print(rows)
#conn.commit()
conn.close()

