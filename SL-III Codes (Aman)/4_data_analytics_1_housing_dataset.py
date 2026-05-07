# Data Analytics-I: Create a Linear 
# Regression Model using Python/R to 
# predict home prices using Boston Housing 
# Dataset. The Boston Housing dataset 
# contains information about various houses 
# in Boston through different parameters. 
# There are 506 samples and 14 feature 
# variables in this dataset. 
# The objective is to predict the value of 
# prices of the house using the given features

# Practical 4: Data Analytics-I (Linear Regression)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.csv"

columns = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD',
           'TAX','PTRATIO','B','LSTAT','MEDV']

df = pd.read_csv(url, names=columns)

# Split into features and target
X = df.drop('MEDV', axis=1)
y = df['MEDV']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy (R² score)
print("Model Accuracy:", model.score(X_test, y_test))