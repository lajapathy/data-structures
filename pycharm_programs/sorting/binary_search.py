
# find a given element in a given sorted list

def bin_search(list1,element):
    if len(list1) == 1:
        return list1[0] == element
    if element == list1[len(list1)/2]:
        return True
    if element < list1[len(list1)/2]:
        return bin_search(list1[:len(list1)/2],element)
    else:
        return bin_search(list1[len(list1) / 2 : ], element)

print bin_search([2,3,4,5],02)