import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans

X = np.loadtxt(fname ='s4.txt')

# plt.scatter(X[:,0], X[:,1], s=2)
# plt.show()
clf = KMeans(n_clusters=15)
clf.fit(X)
centroids = clf.cluster_centers_
labels = clf.labels_
colors = 100*['g.','r.','c.','b.','k.','y.','m.']

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]],markersize =2)
plt.scatter(centroids[:,0],centroids[:,1], marker = 'x', s = 150, linewidths=5)
plt.show()