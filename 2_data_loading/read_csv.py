# Reading CSV files with pandas

#create or download a sample CSV file named 'sample_data.csv' before running this code

import pandas as pd

# df is a variable name , shortly known as dataframe
df= pd.read_csv("data_cleaning_sample.csv")          # This will read the CSV file and store it in a DataFrame
print(df)                                            # prints the dataframe


