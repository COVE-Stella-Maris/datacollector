from bs4 import BeautifulSoup
import requests
import psycopg2
import datetime
from pytz import timezone


title = []
dataHeaders = []
localDateTime = []
avgWindDir = []
avgWindSpd = []
windObs = []
avgSeas = []
waveObs = []


# Request to Page
page = requests.get('https://www.ndbc.noaa.gov/sar.php?station=44258')
#page = requests.get('https://www.ndbc.noaa.gov/sar.php?station=44258&list=all')
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
        date = td.find_next().text
        zTime = td.find_next().find_next().text
        # Local Time Conversion
        zTime = abs(int(zTime[0] + zTime[1]))
        nativeDateTime = datetime.datetime(int(date[6] + date[7] + date[8] + date[9]), int(date[0] + date[1]), int(date[3] + date[4]), zTime, 0, 0)
        print(nativeDateTime)
        localDateTime.append(nativeDateTime)
        # All of the rest of the data
        avgWindDir.append(td.find_next().find_next().find_next().text)
        avgWindSpd.append(td.find_next().find_next().find_next().find_next().text)
        windObs.append(td.find_next().find_next().find_next().find_next().find_next().text)
        avgSeas.append(td.find_next().find_next().find_next().find_next().find_next().find_next().text)
        waveObs.append(td.find_next().find_next().find_next().find_next().find_next().find_next().find_next().text)



# Connecting to Database
conn = psycopg2.connect(host="localhost", database="DataScrapingDB", user="Emerson", password="postgres")
curr = conn.cursor()
removal = "delete from testerdb"

# Populating Databasea
x = 0
while x < len(localDateTime):
    curr.execute("insert into testerdb (datetime,avgWindDir,avgWindSpd,windObs,avgSeas,waveObs) values (%s,%s,%s,%s,%s,%s)",
                 (localDateTime[x],avgWindDir[x],avgWindSpd[x],windObs[x],avgSeas[x],waveObs[x]))
    x = x + 1
var = curr.execute("select * from testerdb")
rows = curr.fetchall()
print(rows)
conn.commit()
conn.close()

