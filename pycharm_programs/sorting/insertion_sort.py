#!/usr/bin/python
# -*- coding: latin-1 -*-

'''
# Step 1 − If it is the first element, it is already sorted. return 1
# Step 2 − Pick next element
# Step 3 − Compare with all elements in the sorted sub-list
# Step 4 − Shift all the elements in the sorted sub-list that is greater than the
#          value to be sorted
# Step 5 − Insert the value
# Step 6 − Repeat until list is sorted
'''
def insertion_sort(list):
    check_till=1
    for i in xrange(1,len(list)):
        for j in xrange(0,check_till):
            if list[i]<list[j]:
                pos = j
                temp = list[i]
                list.remove(list[i])
                list.insert(pos, temp )
                break

        check_till += 1

    return list


print insertion_sort([4,4,24,12,5,1,2])
