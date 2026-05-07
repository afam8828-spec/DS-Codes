
# Data Wrangling-II: Create a synthetic 
# "Academic Performance" dataset for 
# students, and then perform various data 
# wrangling operations in Python. The tasks 
# will involve: 
# 1. Scanning the dataset for missing 
# values and inconsistencies, and 
# handling them. 
# 2. Identifying and dealing with outliers 
# in numeric variables. 
# 3. Applying data transformations on 
# at least one variable for better 
# understanding or to improve 
# distribution. 


# # 1. Import Libraries
# 


import pandas as pd
import numpy as np

# # 2. Create Synthetic Academic Dataset
# 


data = {
    'Student ID': range(1, 101),
    'Age': np.random.randint(18, 25, 100),
    'Gender': np.random.choice(['Male', 'Female'], 100),
    'Subject 1': np.random.randint(50, 100, 100),
    'Subject 2': np.random.randint(60, 90, 100),
    'Subject 3': np.random.randint(55, 95, 100),
    'Attendance': np.random.uniform(70, 100, 100),
    'Final Grade': np.random.choice(['A', 'B', 'C'], 100)
}

df = pd.DataFrame(data)

# # 3. Introduce Missing Values
# 


df.loc[5, 'Subject 1'] = np.nan
df.loc[20, 'Subject 2'] = np.nan
df.loc[35, 'Attendance'] = np.nan

# # 4. Check Missing Values
# 


print("Missing Values:\n", df.isnull().sum())


# # 5. Handle Missing Values
# 


df['Subject 1'] = df['Subject 1'].fillna(df['Subject 1'].mean())
df['Subject 2'] = df['Subject 2'].fillna(df['Subject 2'].median())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean())

# # 6. Handle Inconsistencies
# 


df['Attendance'] = df['Attendance'].clip(0, 100)

df['Final Grade'] = df['Final Grade'].apply(
    lambda x: x if x in ['A', 'B', 'C'] else 'C'
)

print("\nMissing Values After Cleaning:\n", df.isnull().sum())


# # 10. Check Skewness Before Transformation
# 


print("\nSkewness before:", df['Subject 1'].skew())


# # 11. Apply Log Transformation
# 


df['Subject 1'] = np.log(df['Subject 1'] + 1)


# # 12. Check Skewness After Transformation
# 


print("Skewness after:", df['Subject 1'].skew())


# # 13. Final Dataset Preview
# 


print("\nFinal Dataset:\n", df.head())