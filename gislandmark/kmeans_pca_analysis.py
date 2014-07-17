import os
import pickle
from time import time
import numpy as np
import csv
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale


def benchmark(estimator, name, data):
    t0 = time()
    estimator.fit(data)
    print('% 9s   %.2fs    %i   %.3f'
          % (name, (time() - t0), estimator.inertia_,
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean',
                                      sample_size=None)))
    return [time() - t0, estimator.inertia_, metrics.silhouette_score(data, estimator.labels_, metric='euclidean', sample_size=None)]


data_dir = 'C:\\Users\\dedge\\Documents\\Research\\cabspottingdata\\'
results_dir = 'C:\\Users\\dedge\\Documents\\Research\\cabspottinganalysis\\'

filenames = os.listdir(data_dir)
for i in range(len(filenames)): #  control range to something smaller like range(3) to avoid processing all files at one shot
    if 'new' not in filenames[i]: # all data files start with 'new'
        continue
    else:
        print('processing %s ...' %filenames[i])

        data = np.loadtxt(data_dir + filenames[i],usecols=(0,1))

        #data = scale(data)

        n_samples, n_features = data.shape

        resultfilename = filenames[i].split('.')[0] + '_results_kmeans_pca.csv'
        estimatorsfilename = filenames[i].split('.')[0] + '_estimators_kmeans_pca.pickle'
        csvfile = open(results_dir + resultfilename, 'wb')
        estfile = open(results_dir + estimatorsfilename, 'wb')
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['n_centers','time','inertia','silhouette_score'])

        estimators = []
        for n_centers in [5,10,15]:
            pca = PCA(n_components=n_centers).fit(data)
            estimator = KMeans(init=pca.components_, n_clusters=n_centers, n_init=1)
            vals = benchmark(estimator,
                          name="PCA-based",
                          data=data)
            vals = [n_centers] + vals
            estimators.append(estimator)
            csvwriter.writerow(vals)

        pickle.dump(estimators,estfile)
        print('finished writing results to %s and estimators to %s ...' %(resultfilename,estimatorsfilename) )
        csvfile.close()
        estfile.close()