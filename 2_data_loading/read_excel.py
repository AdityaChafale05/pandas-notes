# Reading Excel files with pandas
# Requires pip install openpyxl

#create or download a sample excel file named 'netflix_subscribers_dataset.xlsx' before running this code.
import pandas as pd

# df is a variable name , shortly known as dataframe
df = pd.read_excel("netflix_subscribers_dataset.xlsx")      # This will read the Excel file and store it in a DataFrame
print(df)                                                    # prints the dataframe   
