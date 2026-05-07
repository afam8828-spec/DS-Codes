'''
 Descriptive Statistics - 
 Measures of Central Tendency and variability:
   Using the Iris dataset. We will: 
   a) Perform operations on the Iris dataset to calculate basic statistical details (percentile, mean, standard deviation, etc.) for different species ('Iris-setosa', 'Iris-versicolor', 'Iris virginica'). 
   b) Use Python to extract and analyze these statistics for each species and understand their distributions.

'''

# Practical 3: Descriptive Statistics (Iris)
import pandas as pd

# Load dataset directly from URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

columns = ['SepalLength','SepalWidth','PetalLength','PetalWidth','Species']
df = pd.read_csv(url, names=columns)

# Display data
print(df.head())

# Group by species and calculate statistics
stats = df.groupby('Species').describe()

print(stats)