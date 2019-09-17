def max_separation(arr):
    leftmin = [-1 for i in xrange(len(arr))]
    rightmax = [-1 for i in xrange(len(arr))]
    leftmin[0] = arr[0]
    for i in xrange(1, len(arr)):
        leftmin[i] = min(leftmin[i-1], arr[i])
    rightmax[-1] = arr[-1]
    for i in xrange(len(arr)-2, 0, -1):
        rightmax[i] = max(rightmax[i + 1], arr[i])
    import pdb;pdb.set_trace()
    rightmax.remove(-1)
    i,j,max_diff = 0,0,-1
    while (i<len(arr) & j<len(arr)):
        if leftmin[i] < rightmax[j]:
            max_diff = max(max_diff, j-i)
            j+=1
        else:
            i+=1
    print max_diff

max_separation([4,7,1,3,8,2])
