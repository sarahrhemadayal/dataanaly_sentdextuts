import pandas as pd
import numpy as np
import quandl

api_key = open('quandlapikey.txt', 'r').read()
df = quandl.get('FMAC/HPI_AK', authtoken=api_key)
print(df.head())

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(fiddy_states[0]) #this is a dataset

df = pd.DataFrame(fiddy_states[0])
for abbv in df.iloc[0:, 1]:
    print("FMAC_HPI_"+abbv)