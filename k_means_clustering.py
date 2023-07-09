# -*- coding: utf-8 -*-
"""K_Means_Clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZHHz9N7gf7Ub01mLapWdAdJu8fteaGZA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# SINCE WE HAVE TO CLUSTER THE DATA WE DON'T NEED TO SPLIT THE DATASET INTO TRAIN AND TEST BECAUSE WE DON'T HAVE ANY DEPENDENT VARIABLE
# LET'S MAKE THE ANNUAL INCOME AND SPENDING SCORE AS FEATURE FOR CLUSTERING THE DATASET
data = pd.read_csv('Mall_Customers.csv', header='infer')
X = data.iloc[:, [3,4]].values

# TO CHOOSE THE OPTIMAL NUMBER OF CLUSTERS TO DIVIDE THE DATASET, WE HAVE TO USE ELBOW METHOD
# WE USE WCSS : WITHIN CLUSTER SUM OF SQAURE
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
  # FOR EACH ITERATION, CREATE NEW KMEANS OBJECT
  # PARAMETERS = (n_clusters, init =  method(to avoid the random select trap use k-means++), random_state)
  kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
  kmeans.fit(X);
  wcss.append(kmeans.inertia_) #.inertia_ will give the wcss value of kmeans objects
plt.plot(range(1,11), wcss)
plt.title("The ELbow Curve")
plt.xlabel('No. of  clusters')
plt.ylabel('WCSS value')

# FROM THE GRAPH WE CAN SEE THAT THE OPTIMAL NUMBER OF CLUSTERS ARE 5
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)

print(y_kmeans)

# VISUALIZING THE CLUSTERS
# FOR CLUSTER 0
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label='cluster1')
# FOR CLUSTER 1
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'yellow', label='cluster2')
# FOR CLUSTER 2
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'blue', label='cluster3')
# FOR CLUSTER 3
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'green', label='cluster4')
# FOR CLUSTER 4
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label='cluster5')
plt.legend()
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=250, color = 'black', label='centroids')

