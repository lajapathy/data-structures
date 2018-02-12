

def merge_lists(sorted_list1,sorted_list2):
    combined_list = []
    while (sorted_list1 != [] and sorted_list2 != []):
        if sorted_list1[0] < sorted_list2[0]:
            combined_list.append(sorted_list1[0])
            del sorted_list1[0]
        else:
            combined_list.append(sorted_list2[0])
            del sorted_list2[0]
    while (sorted_list1 != []):
        combined_list.append(sorted_list1[0])
        del sorted_list1[0]

    while (sorted_list2 != []):
        combined_list.append(sorted_list2[0])
        del sorted_list2[0]

    return combined_list

def merge_sort(list):
    if len(list) == 1:
        return list
    else:
        list1 = list[0:int(len(list)/2)]
        list2 = list[int(len(list)/2):]
        return merge_lists(merge_sort(list1),merge_sort(list2))

print (merge_sort([8,2,3,1]))