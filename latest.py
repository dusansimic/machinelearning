from sklearn.ensemble import ExtraTreesClassifier
import numpy as np

trainingFeatures = []
trainingLabels = []
testFeatures = []
fl = []
TR2 = []
TE2 = []
N = 0
print"array"
trainingFile = open("C:/Users/admin/Desktop/Petnica/train.csv", "r")
testFile = open("C:/Users/admin/Desktop/Petnica/test.csv", "r")
next(trainingFile)
next(testFile)
print"files opened"

for trainingLine in trainingFile:
    N += 1
    TR1 = trainingLine.split(',')
    for i in range(0, len(TR1)):
        TR2.append(float(TR1[i]))
        fl.append(TR2)
    TR1 = []
    TR2 = []
print"training input"

np.random.shuffle(fl)
for i in range(0, N):
    trainingFeatures.append(fl[i][:-1]) #if not fl[i][-1] == 8 and not fl[i][-1] == 7:
    trainingLabels.append(fl[i][-1])
print "training done"

for testLine in testFile:
    TE1 = testLine.split(',')
    for i in range(0, len(TE1)):
        TE2.append(float(TE1[i]))
    testFeatures.append(TE2)
    TE1 = []
    TE2 = []  

print "datasets generated"
model = ExtraTreesClassifier(n_estimators=1000, bootstrap=True, class_weight='balanced', oob_score=True, min_impurity_split = 1e-5, criterion = 'entropy')
print "model defined"
model.fit(trainingFeatures, trainingLabels)
print "model fitted"
pred = model.predict(testFeatures)
co = 0

with open('3.txt', 'w') as outputFile:
    for i in range(len(testFeatures)):
        outputFile.write(str(int(pred[i])) + '\n')
trainingFile.close()
testFile.close()
