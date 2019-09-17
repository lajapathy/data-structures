
#works with python3 only

def outer():
    x = 3
    def inner():
        nonlocal x
        x = 2
        print (x)
    print (x)


outer()

