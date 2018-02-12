
#Reverse a list/stack using recursion

list1=[2,3,4,5,6]

def reverse_list(list1):

    if len(list1)==1:
        print list1
        return list1
    else:
        temp_list=list1[:-1]
        stack_top = list1.pop()
        print [stack_top]
        x=reverse_list(temp_list)
        if x:
            return x.extend([stack_top])




print reverse_list(list1)