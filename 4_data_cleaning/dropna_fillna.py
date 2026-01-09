
#Requires knowledge of  numpy
import pandas as pd
import numpy as np

data1= {
    "Name": ["A", "B", "C", "D"],
    "Age": [20, np.nan, 22, np.nan],
    "Marks": [85, 90, np.nan, 88]
}

df =pd.DataFrame(data1)

print("Original DataFrame:\n", df)

#Dropping rows with missing values
print("\n Drop rows with missing values:")
print(df.dropna())

# Drop columns with missing values
print(df.dropna(axis=1) )        
print(" ")


#filling missing values with zero
print("\n fill missing values with zero:")
print(df.fillna(0))
print(" ")


# Fill missing values with column mean
print("\nFill missing values with mean:")
print(df["Age"].fillna(df["Age"].mean()))

print(" ")

# Forward fill missing values
print(df.ffill())
print(" ")

# Backward fill missing values
print(df.bfill())
print(" ")