import pandas as pd

#creating a data_1
data1 = {'Name':['nisha','rohan','jack','monu','manoj'],
       'age':[45,26,35,24,33],
       'country':['usa','malaysia','japan','uganda','india'] }    

#creating a data_2
data2 = {'Name':['rohan','jack','monu','manoj'],
       'age':[45,26,35,33],
       'country':['england','malaysia','uganda','india'] }  

#Creating a series from the given data
print("\n Series ")
series = pd.Series(data1)        # converts data1 into a series
print(series)                    #prints data1 in series format

#Creating a dataframe from the given data
print("\n DataFrame ")
df = pd.DataFrame(data2)      # converts data2 into a dataframe ,   df is the variable name
print(df)