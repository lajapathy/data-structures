#A sorted array has been rotated so that the elements might appear in the order 3 4 5 6 7 1 2.
#  How would you find the minimum element

def find_min(list):
    min=list[0]
    for i in xrange(len(list)):
