
# Data Visualization II: On Titanic dataset  
# 1. Plot a box plot for distribution of age with 
# respect to each gender along with the 
# information about whether they survived or 
# not. (Column names : 'sex' and 'age') 
# 2. Write observations on the inference from 
# the above statistics. 

# Practical 9: Data Visualization II

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('titanic')

# Box plot
plt.figure(figsize=(10,6))
sns.boxplot(x='sex', y='age', hue='survived', data=df)

# Labels
plt.title("Age Distribution by Gender and Survival")
plt.xlabel("Gender")
plt.ylabel("Age")

plt.show()