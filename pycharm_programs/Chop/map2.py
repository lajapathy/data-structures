

list1=[4,3,4,5,6]
tuple1=(4,10,5,2,20)
tuple2=(3,11,4,3,19)
list2 = [1,4,3,6,4]


print (reduce(lambda x : x , zip(list1,list2)))