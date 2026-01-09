
import pandas as pd

# Sample DataFrame with duplicates
df = pd.DataFrame({
    "Name": ["A", "B", "B", "C", "A"],
    "Marks": [85, 90, 90, 78, 85]
})

#true for duplicate rows
print(df.duplicated())

print