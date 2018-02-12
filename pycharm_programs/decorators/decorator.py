import time
import pdb

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, *kwargs)
        end_time = time.time()
        time_taken = (end_time - start_time)*1000
        print (time_taken)
        return result
    return wrapper

@calculate_time
def calc_square(array):
    result = []
    for num in array:
        result.append(num*num)
    return result

@calculate_time
def calc_cube(array):
    result = []
    for num in array:
        result.append(num*num*num)
    return result

arr = range(3)
pdb.set_trace()
calc_square(arr)
#calc_cube(arr)