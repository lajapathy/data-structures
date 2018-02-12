
def outer():
    x=1

    def inner():
        print("inner")
        print(x)

    print("outer")
    return inner

import pdb;pdb.set_trace()
f=outer()
import time;time.sleep(2)

f()