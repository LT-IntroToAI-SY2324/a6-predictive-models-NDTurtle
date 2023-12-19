import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load the dataset
data = pd.read_csv("final-project/traffic_data.csv")

# Extract the features (independent variable)
x = data[["temp", "traffic_volume"]]

# Standardize the data
x_std = StandardScaler().fit_transform(x)

# The value of k has been defined for you
k = 3  # Adjust the number of clusters as needed

# Apply the KMeans algorithm
km = KMeans(n_clusters=k).fit(x_std)

# Get the centroid and label values
centroids = km.cluster_centers_

# Set the size of the graph
plt.figure(figsize=(8, 6))

# Use a for loop to plot the data points in each cluster
labels = km.labels_
for i in range(k):
    cluster = x_std[labels == i]
    plt.scatter(cluster[:, 0], cluster[:, 1], label=f'Cluster {i + 1}')

# Plot the centroids
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=100,
            c='r', label='Centroid')

# Show the graph
plt.xlabel("Temperature (Standardized)")
plt.ylabel("Traffic Volume (Standardized)")
plt.title("KMeans Clustering: Temperature vs. Traffic Volume")
plt.legend()
plt.show()
