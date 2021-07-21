from bs4 import BeautifulSoup
import requests
import psycopg2
import datetime


title = []


# Request to Page
page = requests.get('https://tides.gc.ca/eng/station?type=0&date=2021%2F07%2F21&sid=382&tz=ADT&pres=2')
soup = BeautifulSoup(page.text, 'lxml')

# Grabbing Page Title
title.append(soup.title.string)

# Grabbing Data from Table
for td in soup.find_all('tr'):
    if td.get('class') == "stationTextData":
        date = td.find_next().text




# Connecting to Database
#conn = psycopg2.connect(host="localhost", database="DataScrapingDB", user="Emerson", password="postgres")
#curr = conn.cursor()

# Populating Databasea
#x = 0
#while x < len(localDateTime):
#    curr.execute("insert into testerdb (datetime,avgWindDir,avgWindSpd,windObs,avgSeas,waveObs) values (%s,%s,%s,%s,%s,%s)",
#                 (localDateTime[x],avgWindDir[x],avgWindSpd[x],windObs[x],avgSeas[x],waveObs[x]))
#    x = x + 1
#var = curr.execute("select * from testerdb")
#rows = curr.fetchall()
#print(rows)
#conn.commit()
#conn.close()
