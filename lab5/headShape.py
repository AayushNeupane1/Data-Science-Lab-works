#  Import pandas and create a DataFrame with columns: Name, Age, Marks. 
# Display the first 5 rows and dataset shape.

import pandas as pd

df=pd.DataFrame({
    'Name':['Aayush','Aastha','Smriti','Jeevan'],
    'Age':[20,21,19,22],
    'Marks':[85,90,78,88]
})

print(df.head())
print("Shape of the dataset:", df.shape)