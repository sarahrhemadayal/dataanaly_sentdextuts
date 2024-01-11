import pandas as pd
import numpy as np
import quandl
import matplotlib.pyplot as pyplot
from matplotlib import style
style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats)

#df = df.set_index('Day')
# if you jusst print the latter, it makes a new temp dataframe, doent overwrite the og
df.set_index('Day', inplace=True)

print(df['Visitors'])
print(df[['Bounce Rate', 'Visitors']])
print(df.Visitors.tolist())
print(np.array(df[['Bounce Rate', 'Visitors']]))
#print(df.Visitors), doesnt work for name spaces cus syntax_err
#df.head()
#df.tail