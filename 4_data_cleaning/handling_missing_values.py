
#required numpy knowledge: NaN (Not a Number) representation of missing values

import pandas as pd
import numpy as np           


data1= {
    "Name": ["A", "B", "C", "D"],
    "Age": [20, np.nan, 22, np.nan],
    "Marks": [85, 90, np.nan, 88]
}

df =pd.DataFrame(data1)

#checking for missing values
print("Missing values (If missing then True):") 
print(df.isnull())                              

#count of missing values in each column
print("\n Count of missing values in each column:")
print(df.isnull().sum())               

#check for non-missing values
print("\n Non-missing values (If not missing then True):")
print(df.notnull())
    