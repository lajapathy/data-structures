
def outer():
    def inner():
        print ("inner")

    print("outer")
    return inner

f = outer()
import time;time.sleep(5)
f()