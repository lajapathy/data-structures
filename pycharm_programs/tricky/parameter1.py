#Explain parameter passing mechanism in Python

def fun1(x):
    print x
    print id(x)
    x=6
    print x
    print id(x)


x=10
print id(x)
fun1(x)

