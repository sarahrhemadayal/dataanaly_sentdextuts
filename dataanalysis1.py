import pandas as pd
import quandl
import numpy as np

df = pd.read_csv(r'C:\Users\rhema\Downloads\ZILLOW-DATA.csv')
print(df.head())

df.set_index('date', inplace=True)
df.to_csv('new0.csv')
df = pd.read_csv('new0.csv', index_col=0)
print(df.head())

df = pd.DataFrame(df['value'])
df.columns=['HPI']
print(df.head())
df.to_csv('new1.csv')

df.to_csv('new2.csv', header=False)
df = pd.read_csv('new2.csv')
df = pd.read_csv('new2.csv', names=['Dates', '77006_HPI'], index_col=0)
df.to_csv('new3.csv')
df = pd.read_csv('new3.csv')
print(df.head())