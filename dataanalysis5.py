import pandas as pd
import numpy as np
import quandl
import pickle

api_key = open('quandlapikey.txt', 'r').read()
#new code from here


def state_list(): 
    code = pd.read_csv('codes.csv')
    code = pd.DataFrame(code)
    return code

def get_data():
    main_df = pd.DataFrame()
    states = state_list()
    for ac in states:
        Area = str(ac)
        Area = Area.strip()
        query = "FMAC/HPI_"+Area
        df = quandl.get(query, authtoken=api_key)

        if main_df.empty:
            main_df = df

        else:
            main_df=main_df.join(df)

    #print(main_df)

    pickle_out = open('states_data.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close

#get_data()
    
pickle_in = open('states_data.pickle', 'rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data)


        


