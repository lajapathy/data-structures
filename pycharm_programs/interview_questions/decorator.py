import time

def calc_time(func):
    def deco_fun(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)

    return deco_fun

@calc_time
def square(x):
    list1 = []
    for i in range(x):
        list1.append(x*x)


@calc_time
def cube(x):
    list1 = []
    for i in range(x):
        list1.append(x*x*x)

square(20000)
cube(20000)