'''
Given an array of n elements which contains elements from 0 to n-1, with any of these numbers appearing any number of
times. Find these repeating numbers in O(n) and using only constant memory space.
'''
import pdb

def find_duplicates(list1):

    zero_encountered = False
    #last_element_duplicate = False
    result = []
    for element in list1:
        #pdb.set_trace()
        if element == 0 and not zero_encountered:
            zero_encountered = True
            continue
        if element == 0 and zero_encountered:
            result.append(0)
            continue
        if list1[abs(element)] < 0:
            result.append(abs(element))
            continue
        if list1[abs(element)] > 0:
            list1[abs(element)] = -list1[abs(element)]
    return result

def find_duplicates2(nums):
    res = []
    for x in nums:
        if nums[abs(x) - 1] < 0:
            res.append(abs(x))
        else:
            nums[abs(x) - 1] *= -1
    return res

print(find_duplicates([1,1,2,3,3,4]))
print(find_duplicates([1,2,3,4,5,5]))
#print(find_duplicates([1,2,3,0,0,16,16]))

print(find_duplicates2([1,2,3,4,5,5]))