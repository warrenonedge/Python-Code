import os
import pickle
from time import time
import numpy as np
import csv
from sklearn import metrics
from sklearn.cluster import AffinityPropagation
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
for i in range(1): # len(filenames) control range to something smaller like range(3) to avoid processing all files at one shot
    if 'new' not in filenames[i]: # all data files start with 'new'
        continue
    else:
        print('processing %s ...' %filenames[i])

        data = np.loadtxt(data_dir + filenames[i],usecols=(0,1))

        #data = scale(data)

        n_samples, n_features = data.shape

        resultfilename = filenames[i].split('.')[0] + '_results_affinity.csv'
        estimatorsfilename = filenames[i].split('.')[0] + '_estimators_affinity.pickle'
        csvfile = open(results_dir + resultfilename, 'wb')
        estfile = open(results_dir + estimatorsfilename, 'wb')
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['damping_factor','time','inertia','silhouette_score'])

        estimators = []
        for damping_factor in [0.5,0.6,0.7,0.8,0.9]:
            estimator = AffinityPropagation(damping=damping_factor)
            vals = benchmark(estimator,
                          name="affinity-propagation", data=data)
            vals = [damping_factor] + vals
            estimators.append(estimator)
            csvwriter.writerow(vals)

        pickle.dump(estimators,estfile)
        print('finished writing results to %s and estimators to %s ...' %(resultfilename,estimatorsfilename) )
        csvfile.close()
        estfile.close()