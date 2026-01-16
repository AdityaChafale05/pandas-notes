

import pandas as pd 


data1 = {'Name':['nisha','rohan','jack','monu','manoj','rohan','jack','monu','manoj'],
       'age':[45,26,35,24,33,56,34,6,2],
       'country':['usa','malaysia','japan','uganda','india','england','malaysia','uganda','india'] }   

df = pd.DataFrame(data1)

#group's the data based on Name and then calculates the mean of age for each group
print( df.groupby("Name")['age'].mean() )   

#group's the data based on Name and then counts the number of occurrences of each country for each group
print( df.groupby("Name")['country'].count() )



