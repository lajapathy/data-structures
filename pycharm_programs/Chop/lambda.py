import re

print(list(map(lambda x,y: [x+y,x-y,x*y],(3,6),(5,9))))

#print map(lambda x,y: re.match('(\d+)',y).group(1),['3','6'],['5','9'])


def square(x):
    return (x ** 2)


def cube(x):
    return (x ** 3)


# funcs = [square, cube]
# for r in range(5):
#     value = map(lambda x: x(r), funcs)
#     print value