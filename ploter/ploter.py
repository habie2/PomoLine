
# import pandas as pd
# import plotly.express as px

# df = pd.read_csv('/Users/javisanzdiaz/Desktop/pomoPlot/report.csv')

# fig = px.line(df, x = 'AAPL_x', y = 'AAPL_y', title='Apple Share Prices over time (2014)')
# fig.show()

import pandas as pd
import plotly.express as px

df = pd.read_csv('/Users/javisanzdiaz/Desktop/pomoPlot/report.csv')

fig = px.bar(df, x = 'date', y = 'minutes', color='task', title='Apple Share Prices over time (2014)')
fig.show()