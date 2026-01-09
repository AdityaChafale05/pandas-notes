
import pandas as pd

#Sample data (data1)
data1 = {'Name':['nisha','rohan','jack','monu','manoj','rohan','jack','monu','manoj'],
       'age':[45,26,35,24,33,56,34,6,2],
       'country':['usa','malaysia','japan','uganda','india','england','malaysia','uganda','india'] }   

#creating Dataframe from given data
df = pd.DataFrame(data1)

#for viewing first 5 rows
print("\nHead")
print(df.head)

#for viewing last 5 rows
print("\nTail")
print(df.tail)

#Get basic info about Dataframe
print("\ninfo")
print(df.info)