import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
N = 0
fl = []
features = []
labels = []
arr2 = []
inFile = open("C:/Users/NESA/Documents/petnica/seminar/test_noclass.csv", "r")
next(inFile)
for line in inFile:
    N += 1
    arr1 = line.split(',')
    for i in range(0, len(arr1)):
        arr2.append(float(arr1[i]))
    fl.append(arr2[:])
    arr1 = []
    arr2 = []
print N
np.random.shuffle(fl)
for i in range(0, N):
    features.append(fl[i][:-1])
    labels.append(fl[i][-1])
    
trainingFeatures, testFeatures, trainingLabels, testLabels = train_test_split(features, labels, test_size = 0.2)
print "datasets generated"

model = ExtraTreesClassifier(n_estimators=1000,min_impurity_split=1e-5,criterion='gini')
print "model defined"
model.fit(trainingFeatures, trainingLabels)
print "model fitted"
pred = model.predict(testFeatures)
hits = 0
co = 0

for i in range(len(testFeatures)):
    	if co < 10: 
		print "-", testLabels[i], "-", pred[i]
		co += 1
	if testLabels[i] == pred[i]: hits += 1

print round(1.0 * hits / len(testFeatures)*100,2),"%"
inFile.close()