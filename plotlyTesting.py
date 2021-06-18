import pandas as pd
import plotly.express as px

dfb = pd.read_csv("testingdb.csv", header=None)

df = dfb.apply(pd.to_numeric, errors='ignore')
rdf = df.head(10)
df = px.data.iris()
fig = px.bar(df, x="sepal_width", y="sepal_length")
#fig = px.bar(rdf, x='numList', y='windSpd')
#fig = px.histogram(df, x="Times", y="Wave Speeds")
fig.show()