import pandas as pd
import plotly.express as px
YEAR = 2023
WEEK = 7    # Week of the year: format -> WW

file_name = f'./report_{YEAR}_{WEEK}.csv'
df = pd.read_csv('./report.csv')
# df = pd.read_csv('/Users/javisanzdiaz/Desktop/pomoPlot/report.csv')

fig = px.bar(df, x = 'date', y = 'hours', color='task', title='Apple Share Prices over time (2014)')
fig.show()