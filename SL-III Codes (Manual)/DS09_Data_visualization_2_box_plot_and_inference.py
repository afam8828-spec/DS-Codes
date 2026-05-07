
# Data Visualization II: On Titanic dataset  
# 1. Plot a box plot for distribution of age with 
# respect to each gender along with the 
# information about whether they survived or 
# not. (Column names : 'sex' and 'age') 
# 2. Write observations on the inference from 
# the above statistics. 


# # 1. Import Libraries
# 


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# # 2. Load Dataset
# 


titanic_data = sns.load_dataset('titanic')


# # 3. Data Preprocessing
# # Remove missing values in 'age' (important for boxplot)


titanic_data = titanic_data.dropna(subset=['age'])

# # 4. Create Box Plot
# 


plt.figure(figsize=(10, 6))
sns.boxplot(
    data=titanic_data,
    x='sex',
    y='age',
    hue='survived'
)
plt.title('Box Plot of Age Distribution by Gender and Survival Status')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.legend(
    title='Survived',
    labels=['Did Not Survive', 'Survived']
)
plt.grid(True)
plt.show()