import numpy as np
import pandas as pd

data={'Student': ['Amit', 'Bhavna', 'Chetan', 'Diya', 'Amit', 'Esha', np.nan],
'Maths': [75, 82, np.nan, 90, 75, 72, 85],
'Python': [80, 78, 70, np.nan, 80, 75, 88],
'Attendance': [85, 90, 78, 95, 85, np.nan, 92],
'City': ['Pune', 'Mumbai', 'Pune', 'Nashik', 'Pune', 'Mumbai', 'Pune']}

df = pd.DataFrame(data)
print("Original DataFrame (With Missing Values & Duplicates)")
print(df)

print("\nDataset Info")
print(df.info())

print("\nMissing Values Count per Column")
print(df.isnull().sum())

df['Maths'] = df['Maths'].fillna(df['Maths'].mean())
df['Python'] = df['Python'].fillna(df['Python'].mean())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean())

df = df.dropna(subset=['Student'])

df = df.drop_duplicates()
print("\nDataFrame After Cleaning & Removing Duplicates")
print(df)


print("\nFiltered Data: Students with Python Marks > 75")
filtered_df = df.loc[df['Python'] > 75]
print(filtered_df)
