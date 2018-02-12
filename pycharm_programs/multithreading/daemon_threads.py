#By setting a thread as a daemon, the thread is killed automatically once main thread completes execution

#Main thread waits for a NOn-DAEMON thread, but NOt for a daemon thread

import threading
import time
import logging

logging.basicConfig(format='(%(threadName) -9s %(message)s', level=logging.DEBUG)

def nd():
    print 'Starting ND thread'
    time.sleep(7)
    print 'Ending ND thread'

def d():
    print 'Starting D thread'
    time.sleep(3)
    print 'Ending D thread'


nd_t = threading.Thread(target = nd, name = 'nd_thread')
d_t = threading.Thread(target = d, name = 'd_thread')
d_t.setDaemon(True)
nd_t.start()
d_t.start()
time.sleep(5)

