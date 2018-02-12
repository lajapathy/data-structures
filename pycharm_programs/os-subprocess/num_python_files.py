import os

#Implement a yield function to return filenames on demand
def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1


def fun1():
    return [file for file in os.listdir(os.getcwd()) if ".py" in file]

y = yrange(5)
print y.next()
print y.next()
print y.next()
print y.next()