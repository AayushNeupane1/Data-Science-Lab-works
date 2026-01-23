#  Select rows where Marks > 60. 
# Select only Name and Marks columns. 

import pandas as pd

df=pd.read_csv('students.csv')
selected_df = df[df['Marks']>60]
selected_columns = selected_df[['Name','Marks']]  
print(selected_columns.to_string(index=False))
# print(type(selected_columns))