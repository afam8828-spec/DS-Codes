# Data Visualization III: On iris dataset give 
# inference as: 
# 1. List down the features and their types 
# (e.g., numeric, nominal) available in the 
# dataset.  
#     
# 2. Create a histogram for each feature in 
# the dataset to illustrate the feature 
# distributions.  
# 3. Create a boxplot for each feature in the 
# dataset. 
# 4. Compare distributions and identify 
# outliers 

# Practical 10: Data Visualization III

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('iris')

# Display dataset
print(df.head())

# Feature types
print(df.dtypes)

# Histograms for all features
df.hist(figsize=(10,8))
plt.suptitle("Histograms of Iris Dataset")
plt.show()

# Boxplot for all features
plt.figure(figsize=(10,6))
sns.boxplot(data=df)
plt.title("Boxplot of Iris Dataset")
plt.show()