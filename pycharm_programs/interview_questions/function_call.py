import threading
import time

def f():
    f.counter += 1
    if f.counter > 2:
        return False
    return True
f.counter = 0

def time_func():
    threading.Timer(5.0, time_func).start()
    print "time_func called"
    f.counter = 0

time_func()

for _ in xrange(5):
    time.sleep(1)
    print f()