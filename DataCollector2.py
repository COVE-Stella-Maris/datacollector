from bs4 import BeautifulSoup
import requests
import psycopg2
import datetime


title = []
data = []


# Request to Page
page = requests.get('https://tides.gc.ca/eng/station?type=0&date=2021%2F07%2F21&sid=382&tz=ADT&pres=2')
soup = BeautifulSoup(page.text, 'lxml')

# Grabbing Page Title
title.append(soup.title.string)

# Grabbing Data from Table
for div in soup.find_all('div', attrs={"class": "stationTextData"}):
    stripper = div.text.replace('\r','')
    stripper = stripper.replace('\n', '')
    stripper = stripper.replace(' ', '')
    data.append(stripper)

print(data)

"""
# Connecting to Database
conn = psycopg2.connect(host="localhost", database="DataScrapingDB", user="Emerson", password="postgres")
curr = conn.cursor()

# Populating Databasea
x = 0
while x < len(data):
    curr.execute("insert into datascraper2 (datetime, heightmetric) values (%s, %i)", (datetime[x], data[x]))
    x = x + 1
var = curr.execute("select * from testerdb")
rows = curr.fetchall()
print(rows)
conn.commit()
conn.close()
"""