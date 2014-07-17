import numpy as np
from sklearn.cluster import KMeans
import pylab as pl
from time import time

infile = open("new_abboip.txt")
infile.readline()
data=np.loadtxt(infile)

tempData = data[:,:2]

n_samples = len(data)
n_features = 2


kmeans = KMeans(init='k-means++', n_clusters=9, n_init=10)
t0 = time()
kmeans.fit(tempData)
t_batch = time() - t0
kmeans_labels = kmeans.labels_
kmeans_cluster_centers = kmeans.cluster_centers_
kmeans_labels_unique = np.unique(kmeans_labels)

fig = pl.figure(figsize=(6, 6))
fig.subplots_adjust(left=0.02, right=0.98, bottom=0.05, top=0.9)
colors = ['#4EACC5','#FF9C34','#4E9A06','#FF0000','#FF00EA','#0008FC','#F400Fc','#15FF00','#FF0099']
ax = fig.add_subplot(1,1,1)
for k, col in zip(range(9), colors):
    my_members = kmeans_labels == k
    cluster_center = kmeans_cluster_centers[k]
    ax.plot(tempData[my_members, 0], tempData[my_members, 1], 'w', markerfacecolor=col, marker='.')
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=6)
ax.set_title('KMeans')
ax.set_xticks(())
ax.set_yticks(())
pl.text(-3.5, 1.8,  'train time: %.2fs\ninertia: %f' % (t_batch, kmeans.inertia_))
pl.show()

