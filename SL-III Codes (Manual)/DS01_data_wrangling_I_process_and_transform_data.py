# Data Wrangling-I: Importing libraries, 
# loading a dataset, preprocessing it, 
# checking for missing values, exploring the 
# dataset, and performing necessary 
# transformations and normalizations to 
# clean the data. 


# 1. Import required libraries



import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

# 2. Load dataset


df = pd.read_csv('titanic.csv')   

# # 3. Explore dataset
#


print("First 5 rows:\n", df.head())

print("\nShape of dataset:", df.shape)

print("\nData Types:\n", df.dtypes)

print("\nStatistical Summary:\n", df.describe())

# # 4. Check missing values
# 


missing_values = df.isnull().sum()
print("\nMissing Values:\n", missing_values)

 # 6. Handle missing values



# Fill Age with mean
df['Age']=df['Age'].fillna(df['Age'].mean())


# # 5. Data preprocessing
# 



# Convert Age to numeric
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Convert Survived to categorical
df['Survived'] = df['Survived'].astype('category')

# # 7. Normalize numerical columns



from sklearn.preprocessing import MinMaxScaler



scaler = MinMaxScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])


# 8. Convert categorical to numerical


# Convert 'Sex' column to numerical (0 = male, 1 = female) 
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1}) 
 
# Convert 'Embarked' column to numerical (using one-hot encoding) 
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)


# 9. Check final dataset

print("\nFinal Data Types:\n", df.dtypes)

print("\nFinal Dataset Preview:\n", df.head())