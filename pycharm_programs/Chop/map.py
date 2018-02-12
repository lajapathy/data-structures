
#Implement map, reduce, filter functionality
#http://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php

def map1(fun,seq):
    tuple1=()
    for item in seq:
        tuple1+=fun(item),
    return tuple1

def filter1(condition,seq):
    tuple1=()
    for item in seq:
        if condition(seq):
            tuple1+=item,

    return tuple1

def reduce1(combine_func,seq):
    result=''
    for item in seq:
        combine_func(item)

def combine_func(items,total=0):
    if len(items)==1:
        return items[0]
    else:
        return items[0] + combine_func(items[1:],total)

list1=[4,3,4,5,6]
tuple1=(4,10,5,2,20)
tuple2=(3,11,4,3,19)
list2 = [1,4,3,6,4]
#print zip(list1,list2)
#print filter(lambda (x,y):x>y, zip(list1,list2))
#print reduce(lambda x,y:x*y, list1)

print filter(lambda (x,y):x>y, zip(list1,list2))
