#  Check for missing values in the dataset. 
# Fill missing numerical values with the mean
import pandas as pd
data={
    'Name':['Aastha','Aayush','Jeevan','Smriti'],
    'Age': [19,18,None,20],
    'Marks':[99,None,97,96]
}
df=pd.DataFrame(data)
print("Missing values in each column:\n", df.isnull().sum())
# print(type(df.isnull()))
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Marks'].fillna(df['Marks'].mean(),inplace=True)
print("\nData after filling missing values:\n", df)