

def selection_sort(list):
    start_index=0
    found_new_min = False
    for i in xrange(len(list)-1):
        min = list[i]
        for j in xrange(i+1,len(list)):
            if list[j] < min:
                found_new_min = True
                min = list[j]
                min_index = j

        #Swap
        if found_new_min:
            old_min = list[i]
            list[i] = min
            list[min_index] = old_min
        found_new_min = False

    return list


print selection_sort([4,5,1,8,6,6,7,3])


