
def insert_element_sorted_list(list,item):
    greater_than = False
    first_item = True
    for i in xrange(len(list)):
        if first_item and (item < list[i]):
            list.insert(i,item)
        if item >= list[i]:
            greater_than=True
        if greater_than and (item < list[i]):
            list.insert(i,item)
        first_item = False
    return list


def sort_stack(stack,curr_item=None):

    if len(stack) == 0:
        return [curr_item]
    temp = stack.pop()
    return insert_element_sorted_list(sort_stack(stack,temp),temp)


list1=[20,3,1,8,19]
print sort_stack(list1)

