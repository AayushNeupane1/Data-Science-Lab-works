# Create a new column by transforming Marks (e.g., Marks / 10).
# Rename columns and save the cleaned dataset to a CSV file.
import pandas as pd
df = pd.read_csv('transform.csv')
df['Transformed_Marks'] = df['Marks']/10
df = df.rename(columns={'Name': 'Std_Name', 'Age': 'Std_Age', 'Marks': 'Original_Marks'})
df.to_csv('cleanedTransform.csv', index=False)
print("Data after transformation and renaming:")
print(df)