
import pandas as pd 

data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [20, 25, 22, 30],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

#filtering marks with condition 
print(df[df["Marks"] > 80] )

#multiple conditions 
print(df[(df['Age'] > 20) & (df['Marks'] > 80)])

## Using isin()
print("\nNames in ['A', 'C']:")
print(df[df["Name"].isin(["A", "C"])])