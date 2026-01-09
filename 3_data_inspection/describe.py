import pandas as pd 

#Sample data (data1)
data1 = {'Name':['nisha','rohan','jack','monu','manoj','rohan','jack','monu','manoj'],
       'age':[45,26,35,24,33,56,34,6,2],
       'country':['usa','malaysia','japan','uganda','india','england','malaysia','uganda','india'] }   

df = pd.DataFrame(data1)      #converting data to Dataframe

print(df.describe())          #Gives statistical summary: count,mean,std,min / max,quartiles
