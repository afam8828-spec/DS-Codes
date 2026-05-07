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

# Practical 2: Data Wrangling-II
import pandas as pd
import numpy as np

# Step 1: Create dataset
df = pd.DataFrame({
    'Student_ID': range(1, 101),
    'Marks': np.random.randint(50, 100, 100),
    'Attendance': np.random.uniform(60, 100, 100)
})

# Step 2: Introduce missing values
df.loc[5, 'Marks'] = np.nan
df.loc[10, 'Attendance'] = np.nan

# Step 3: Check missing values
print("Missing Values:\n", df.isnull().sum())

# Step 4: Handle missing values
df['Marks'].fillna(df['Marks'].mean(), inplace=True)
df['Attendance'].fillna(df['Attendance'].mean(), inplace=True)

# Step 5: Detect outliers using IQR
Q1 = df['Marks'].quantile(0.25)
Q3 = df['Marks'].quantile(0.75)
IQR = Q3 - Q1

# Step 6: Remove outliers using clipping
df['Marks'] = np.clip(df['Marks'], Q1 - 1.5*IQR, Q3 + 1.5*IQR)

# Step 7: Apply transformation (log)
df['Marks'] = np.log(df['Marks'])

# Final dataset
print(df.head(10))

