#  Detect duplicate rows in the dataset. 
# Remove duplicates and verify the result. 

import pandas as pd 

dup_Data={
    'Name':['Aastha','Aayush','Jeevan','Smriti','Aastha','Jeevan'],
    'Age': [19,18,17,20,19,17],
    'Marks': [99,98,97,96,99,97]
} 

print("Original DataFrame:")
df=pd.DataFrame(dup_Data)
print(df)

duplicates = df.duplicated()
print("\nDuplicate rows in the DataFrame:\n", df[duplicates])

df_no_duplicates = df.drop_duplicates()
print("\nDataFrame after removing duplicates:\n", df_no_duplicates)