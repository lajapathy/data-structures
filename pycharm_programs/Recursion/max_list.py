#given a list, find max element in list recursively

def find_max(list1,max=None):
    if list1 == []:
        return max
    if not max:
        return find_max(list1[1:],list1[0])
    if list1[0] <= max:
        return find_max(list1[1:],max)
    else:
        return find_max(list1[1:], list1[0])


print find_max([3,5,7,11,2,7,4])