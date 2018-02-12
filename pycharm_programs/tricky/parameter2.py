
#When does Python parameter passing work like "pass by reference"
#Answer : When paramters are mutable type

def fun1(list1):
    print id(list1)
    list1.append(4)
#    list1+=[4]
    print id(list1)

# list1=[1,2,3]
# print id(list1)
# fun1(list1)
# print list1

list2=[1,2,3]
print id(list2)
fun1(list2)
print list2
