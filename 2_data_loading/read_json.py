# Reading a json file with pandas

# create or download a sample json file named 'sample1.json' before running this code

import pandas as pd

# df is a variable name , shortly known as dataframe
df = pd.read_json("sample1.json")               # This will read the json file and store it in a DataFrame
print(df)                                     # prints the dataframe