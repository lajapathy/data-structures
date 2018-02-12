import time

def calc_time(func):
    def deco_fun(*args, **kwargs):
        list1 = []
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)

    return deco_fun

@calc_time
def square(x):

    for i in range(x):
        list1.append(x*x)


@calc_time
def cube(x):

    for i in range(x):
        list1.append(x*x*x)
    list1=[1,8,27]

square(20000)
#cube(20000)