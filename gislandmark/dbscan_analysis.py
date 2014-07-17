import os
import pickle
from time import time
import numpy as np
import csv
from sklearn import metrics
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


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

        data = StandardScaler().fit_transform(data)

        n_samples, n_features = data.shape

        resultfilename = filenames[i].split('.')[0] + '_results_dbscan.csv'
        estimatorsfilename = filenames[i].split('.')[0] + '_estimators_dbscan.pickle'
        csvfile = open(results_dir + resultfilename, 'wb')
        estfile = open(results_dir + estimatorsfilename, 'wb')
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['epsilon','time','inertia','silhouette_score'])

        estimators = []
        for epsilon in [0.01,0.05,0.1,0.2,0.3]:
            estimator = DBSCAN(eps=epsilon, min_samples=10)
            vals = benchmark(estimator,
                          name="dbscan", data=data)
            vals = [epsilon] + vals
            estimators.append(estimator)
            csvwriter.writerow(vals)

        pickle.dump(estimators,estfile)
        print('finished writing results to %s and estimators to %s ...' %(resultfilename,estimatorsfilename) )
        csvfile.close()
        estfile.close()