def ConvexHull(bucket):
    bucket = bucket.tolist()
    min_x = bucket[0]
    max_x = bucket[0]

    #Find point with minimum x and maximum x => O(N)
    for point in bucket:
        if (point[0] > max_x[0]):
            max_x = point
        if (point[0] < min_x[0]):
            min_x = point

    #Divide into two set (left and right of line) => O(N)
    left_batch = []
    right_batch =[]
    for point in bucket:
        sideVal = distance(min_x,max_x,point)
        if(sideVal > 0): #Point on the right side of line min_x--max_x
            right_batch+=[point]
        if(sideVal < 0): #Point on the left side of line min_x--max_x
            left_batch+=[point]
    result = []
    print(left_batch)
    print(min_x,max_x)
    return result

def distance(begin_point, end_point, eval_point): #if on the right side, value > 0 ; if left side value < 0 ; else on the line => O(1)
    #Using Cross-Product on 2D 
    return ((end_point[0] - begin_point[0])*(begin_point[1]-eval_point[1]) - (end_point[1] - begin_point[1])*(begin_point[0]-eval_point[0]))

def QuickHull(begin_point, end_point,bucket):
    result = []
    if bucket.length == 0:
        return result
    return

import pandas as pd
from sklearn import datasets
data = datasets.load_iris() 
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
bucket = df[df['Target'] == 0]
bucket = bucket.iloc[:,[0,1]].values
ConvexHull(bucket)