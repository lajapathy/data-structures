#Sort a stack using recursion
#Allowed methods : peek, push , pop, isEmpty

import stack

s=stack()
stack.push(5)
stack.push(8)
stack.push(1)
stack.push(3)
stack.push(6)
stack.push(2)

s2=stack()

def sort_stack(stack_list1,stack_list2):
    if len(stack_list1) == 1:

        stack_list2.append(stack_list1.pop())
        return stack_list2
    if stack_list1[0]>stack_list2[0]:
        stack_list1.append(stack_list2.pop())
    else:
        sort_stack(stack_list2.pop(),stack_obj2.pop())



