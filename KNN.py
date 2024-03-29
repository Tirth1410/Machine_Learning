# -*- coding: utf-8 -*-
"""KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WxY0r9nalI3dt5051SdK8QgFuq6Y5AHl
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Social_Network_Ads.csv', header='infer')
X = data.iloc[:,1:-1].values
y = data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#Feature Scaling data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#KNN model import
from sklearn.neighbors import KNeighborsClassifier
#PARAMETER
# n_neighbors
# weights = 'uniform'(equal weights) or 'distance'(inverse of distance = weight)
# algorithm = 'BallTree' or 'KD' or 'bruteforce' or 'auto'(best or suitable from previous 3)
# p = Power variable
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p=2)

classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

print(np.concatenate((y_test.reshape(len(y_test),1), y_pred.reshape(len(y_pred), 1)), 1))

#Making confusion matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))

