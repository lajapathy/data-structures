import pdb

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dict1 = {}
    max = 1
    min = 1
    for element in nums:
        if element <0 :
            continue
        if element > max:
            max = element
        if element < min:
            min = element
        dict1[element] = 10
    #pdb.set_trace()
    while min < max:
        if min in dict1.keys():
            min = min + 1
            continue
        else:
            return min
    return max + 1

print(firstMissingPositive([3,4,-1,1]))
print(firstMissingPositive([1,2,0]))
print(firstMissingPositive([3,5,-1,1]))

