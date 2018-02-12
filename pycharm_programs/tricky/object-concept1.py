

list1 = [2,3,4]
list2=list1

print list1
print list2
print id(list1)
print id(list2)


list2.append(5)
print list1
print list2
print id(list1)
print id(list2)

d={1:2,3:4}
e=d.copy()
print e
f=d
print d
print f
print id(d)
print id(e)
print id(f)