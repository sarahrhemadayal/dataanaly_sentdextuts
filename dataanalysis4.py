import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])


#merging: checks index/s mentioned and merges based index (so matching index is super important, else err)
df4 = pd.merge(df1, df2, on=['HPI', 'Int_rate'])
print(df4)
print(pd.merge(df1, df3)) #stacks but no error as matching index

#joining (basically fancy merging)
df1.set_index('HPI', inplace=True)
df2.set_index('HPI', inplace=True)
print(pd.merge(df1, df2, how='inner'))