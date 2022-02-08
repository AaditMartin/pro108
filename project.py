import pandas as pd
import plotly.figure_factory as ff
import csv
df=pd.read_csv('prodata.csv')
graph=ff.create_distplot([df['ar'].tolist()],['Ar'])
graph.show()