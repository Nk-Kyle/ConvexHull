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
    left_batch,right_batch = divideSet(min_x,max_x,bucket)

    #Conquer (Counter ClockWise to maintain order always use right set of oriented line)
    return [min_x] + QuickHull(min_x,max_x, right_batch) + [max_x] + QuickHull(max_x,min_x,left_batch) 
    

def distance(begin_point, end_point, eval_point): #if on the right side, value > 0 ; if left side value < 0 ; else on the line => O(1)
    #Using Cross-Product on 2D 
    return ((end_point[0] - begin_point[0])*(begin_point[1]-eval_point[1]) - (end_point[1] - begin_point[1])*(begin_point[0]-eval_point[0]))

def divideSet(begin_point,end_point,bucket):
    left_batch = []
    right_batch =[]
    for point in bucket:
        sideVal = distance(begin_point,end_point,point)
        if(sideVal > 0): #Point on the right side of line min_x--max_x
            right_batch+=[point]
        if(sideVal < 0): #Point on the left side of line min_x--max_x
            left_batch+=[point]
    return left_batch,right_batch

def QuickHull(begin_point, end_point,bucket):
    n_points = len(bucket)
    if n_points == 0:
        return []
    elif n_points == 1:
        return [bucket[0]]
    else:
        furthest_dist = 0
        furthest_point = bucket[0]

        #find furthest point from oriented line => O(N)
        for point in bucket:
            if (abs(distance(begin_point,end_point,point)) > furthest_dist):
                furthest_dist = abs(distance(begin_point,end_point,point))
                furthest_point = point
        
        #divide into two triangle parts ("upper left" and "upper right")
        #Get "upper right" set
        temp_set, upright_set = divideSet(begin_point,furthest_point,bucket)
        #Get "upper left" set
        temp_set, upleft_set = divideSet(furthest_point,end_point,temp_set)
        return QuickHull(begin_point,furthest_point,upright_set) + [furthest_point] + QuickHull(furthest_point,end_point,upleft_set) 