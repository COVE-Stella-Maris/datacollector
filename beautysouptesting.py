from bs4 import BeautifulSoup
import requests
import psycopg2
import datetime


title = []
dataHeaders = []
date = []
UTC = []
avgWindDir = []
avgWindSpd = []
windObs = []
avgSeas = []
waveObs = []


# Request to Page
page = requests.get('https://www.ndbc.noaa.gov/sar.php?station=44258&list=all')
soup = BeautifulSoup(page.text, 'lxml')

# Grabbing Page Title
title.append(soup.title.string)

# Grabbing Data Headers
for th in soup.find_all('th'):
    dataHeaders.append(th.text.strip())
#print(dataHeaders)

# Grabbing Data from Table
for td in soup.find_all('tr'):
    if td.get('bgcolor') == "#f0f8fe" or td.get('bgcolor') == "#fffff0":
        date.append(td.find_next().text)
        localTime = td.find_next().find_next().text
        localTime = int(localTime[0:4])
        localTime = abs((localTime - 1200) - 300)
        UTC.append(localTime)
        avgWindDir.append(td.find_next().find_next().find_next().text)
        avgWindSpd.append(td.find_next().find_next().find_next().find_next().text)
        windObs.append(td.find_next().find_next().find_next().find_next().find_next().text)
        avgSeas.append(td.find_next().find_next().find_next().find_next().find_next().find_next().text)
        waveObs.append(td.find_next().find_next().find_next().find_next().find_next().find_next().find_next().text)
print(datetime.datetime.now())
print(UTC)


# Connecting to Database
conn = psycopg2.connect(host="localhost", database="DataScrapingDB", user="Emerson", password="postgres")
curr = conn.cursor()
curr.execute("delete from testerdb where id>=0")

# Populating Databasea
x = 0
while x < len(date):
    curr.execute("insert into testerdb (id,date,time,avgWindDir,avgWindSpd,windObs,avgSeas,waveObs) values (%s, %s,%s,%s,%s,%s,%s,%s)",
                 (x,date[x],UTC[x],avgWindDir[x],avgWindSpd[x],windObs[x],avgSeas[x],waveObs[x]))
    x = x + 1
var = curr.execute("select * from testerdb")
rows = curr.fetchall()
print(rows)
conn.commit()
conn.close()

