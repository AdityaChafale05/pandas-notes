
import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [20, 25, 22, 30],
    "Marks": [85, 90, 78, 88]
}
df = pd.DataFrame(data)

#sort by marks
df1 = df.sort_values(by="Marks")
print(df1)

#multiple columns 
df2 = df.sort_values(by=["Age","Marks"], ascending=[True, False])
print(df2)
