'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
'''

def find_threesum(list1, sublist=[]):

    result = []
    n = len(list1)
    #base case
    if len(sublist)==3 and sum(sublist) == 0:
        import pdb;pdb.set_trace()
        return sublist

    for i in range(n):
        return find_threesum(list1[:i]+list1[i+1:], sublist.append(list1[i]))



print(find_threesum([-1, 0, 1, 2, -1, -4]))
