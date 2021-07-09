import pandas as pd
import plotly.express as px
import psycopg2

data = []
time = []

conn = psycopg2.connect(host="localhost", database="DataScrapingDB", user="Emerson", password="postgres")
if(conn):
    print("Connected")
curr = conn.cursor()
var = curr.execute("select * from testerdb")
rows = curr.fetchall()
x = 0
while x < len(rows):
    data.append(int(rows[x][1]))
    time.append(int(x))
    x = x + 1
testGraph = px.line(x=time, y=data, labels={'x':'Time','y':"Avg Wind D"})
testGraph.show()
print(data)

conn.commit()
conn.close()