# Data Analytics-III 1. Implement Simple Naïve Bayes classification algorithm using Python/R on iris.csv dataset. 2. Compute Confusion matrix to find TP, FP, TN, FN, Accuracy, Error rate, Precision, Recall the given dataset. 


# # 1. Import Libraries
# 


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score



# # 2. Load Dataset
# 


df = pd.read_csv('iris_dataset.csv')
print("First 5 rows:\n", df.head())
print("\nMissing Values:\n", df.isnull().sum())

# # 3. Preprocessing
# 


X = df.iloc[:, :-1].values   # Features
y = df.iloc[:, -1].values    # Target

# # 4. Train-Test Split
# 


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


# # 5. Train Naïve Bayes Model
# 


model = GaussianNB()
model.fit(X_train, y_train)

# # 6. Prediction
# 


y_pred = model.predict(X_test)


# # 7. Confusion Matrix
# 


cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

# # 8. Performance Metrics
# 


accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
error_rate = 1 - accuracy
print("\nAccuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("Error Rate:", error_rate)

# # 9. Confusion Matrix Visualization
# 


plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=model.classes_,
            yticklabels=model.classes_)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()