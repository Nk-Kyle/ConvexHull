import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import uniform
from sklearn import datasets

print("\nChoose number for your dataset to Test Linear Separability Dataset")
print("(Below chosen datasets from sklearn which has class / separable)")
print(
    '''
    1. iris
    2. wine
    3. breast_cancer
    '''
)
print("(Below chosen datasets from sklearn which is not separable (no classes))")
print(
    '''
    4. boston
    5. diabetes
    '''
)

while(True):
    n = int(input("Chosen data number: "))
    if(n == 1):
        data = datasets.load_iris() 
        break
    elif(n == 2):
        data = datasets.load_wine() 
        break
    elif(n == 3):
        data = datasets.load_breast_cancer() 
        break
    elif(n == 4):
        data = datasets.load_boston()
        break
    elif(n == 5):
        data = datasets.load_diabetes()
        break
    else: print("Invalid Number!")

print("\nHere are the list of features of this data collection:\n")
for i in range(len(data.feature_names)):
    print(str(i+1) + "." +data.feature_names[i])
first_feature = int(input("Choose first feature: "))-1
second_feature = int(input("Choose second feature: "))-1
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)

from myConvexHull import ConvexHull
plt.figure(figsize = (10, 6))
colors = ['b','r','g','c','m','y']
plt.title(str(data.feature_names[first_feature])+" vs "+str(data.feature_names[second_feature]))
plt.xlabel(data.feature_names[first_feature])
plt.ylabel(data.feature_names[second_feature])

try :
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[first_feature,second_feature]].values
        hull = ConvexHull(bucket)
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i],color =colors[i%6])
        hul_len = len(hull)
        plt.plot([row[0] for row in hull]+[hull[0][0]], [row[1] for row in hull]+[hull[0][1]],color =colors[i%6])
    plt.legend()
except:
    bucket = df
    bucket = bucket.iloc[:,[first_feature,second_feature]].values
    hull = ConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1],color =colors[0])
    hul_len = len(hull)
    plt.plot([row[0] for row in hull]+[hull[0][0]], [row[1] for row in hull]+[hull[0][1]],color =colors[0])
plt.show()