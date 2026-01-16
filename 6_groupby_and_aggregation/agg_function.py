
import pandas as pd 


data1 = {'Name':['nisha','rohan','jack','monu','manoj','rohan','jack','monu','manoj'],
       'age':[45,26,35,24,33,56,34,6,2],
       'country':['usa','malaysia','japan','uganda','india','england','malaysia','uganda','india'] }   

df = pd.DataFrame(data1)


#distribute the data into groups based on Name and then apply multiple aggregation functions (mean, max, min) on the age column for each group
print( df.groupby("Name")['age'].agg(['mean','max','min']) ) 

#inshort - gives values of mean, max and min in single line


