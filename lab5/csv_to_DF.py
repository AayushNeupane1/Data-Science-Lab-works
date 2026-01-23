#  Load a CSV file into a DataFrame. 
# Display column names, data types, and basic statistics.

import pandas as pd

data={
    'Name':['Aastha','Aayush','Jeevan','Smriti','Shyam','Sani','Aavashey'],
    'Age': [19,18,17,20,21,20,20],
    'Marks': [99,98,97,96,95,64,50]
}
    
df = pd.DataFrame(data)
df.to_csv('students.csv',index=False)


df = pd.read_csv('students.csv')
print("Column names:\n", df.columns)
print("Data types:\n", df.dtypes)
print("Basic statistics:\n", df.describe().round(2))