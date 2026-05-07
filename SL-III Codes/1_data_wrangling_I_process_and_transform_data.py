# Data Wrangling-I: Importing libraries, 
# loading a dataset, preprocessing it, 
# checking for missing values, exploring the 
# dataset, and performing necessary 
# transformations and normalizations to 
# clean the data. 

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load dataset
url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# # Display first rows
# print(df.head())

# # Check missing values
# print(df.isnull().sum())

# Fill missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Convert categorical to numeric
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# One-hot encoding
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# Normalize data
scaler = MinMaxScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Final dataset
print(df.head())