import threading

def f(i):
    print 'thread function '+str(i)
    print threading.currentThread().getName()
    return

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f,args=(i,))
        # NOTE : START method of the threading.Thread object can be called only once
        t.start()

