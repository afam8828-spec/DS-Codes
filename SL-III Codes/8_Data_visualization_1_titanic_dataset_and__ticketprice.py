# Data Visualization I: 1. Use the inbuilt 
# dataset 'titanic'. The dataset contains 891 
# rows and contains information about 
# the passengers who boarded the 
# unfortunate Titanic ship. Use the Seaborn 
# library to see if we can find any patterns in 
# the data. 
# 2. Write a code to check how the price of 
# the ticket (column name: 'fare') for each 
# passenger is distributed by plotting a 
# histogram. 

# Practical 8: Data Visualization I

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('titanic')

# Display first rows
print(df.head())

# Summary
print(df.describe())

# Histogram of fare
plt.figure(figsize=(10,6))
sns.histplot(df['fare'], kde=True, bins=30)

# Labels
plt.title("Distribution of Titanic Ticket Prices (Fare)")
plt.xlabel("Fare")
plt.ylabel("Frequency")

plt.show()

