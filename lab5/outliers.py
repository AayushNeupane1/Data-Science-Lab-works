#  Identify outliers in the Marks column using the IQR method. 
# Remove the outliers from the dataset.

import pandas as pd

data = {
    'Name': ['Aastha', 'Aayush', 'Jeevan', 'Smriti', 'Shyam', 'Sani', 'Aavashey', 'Rohan'],
    'Age': [19, 18, 17, 20, 21, 20, 20, 22],
    'Marks': [99, 98, 97, 96, 95, 64, 50, 150] 
}

df = pd.DataFrame(data)
Q1 = df['Marks'].quantile(0.25)
Q3 = df['Marks'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR    
outliers = df[(df['Marks'] < lower_bound)|(df['Marks'] > upper_bound)]
print("Outliers in the Marks column:\n", outliers)
df_no_outliers = df[(df['Marks']>=lower_bound)&(df['Marks'] <= upper_bound)]
print("\nDataFrame after removing outliers:\n",df_no_outliers)