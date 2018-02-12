import thread
import time
import random



def fun1(threadName, delay):
    print 'Inside fun'
    count = 0
    while (count < 5):
        print 'Inside while'
        time.sleep(delay)
        print ("%s : %s") %(threadName, time.ctime(time.time()))
        count +=1

try:
    thread.start_new_thread(fun1,('thread1',2))
    thread.start_new_thread(fun1,('thread2',1))
except Exception,e:
    print 'Unable to start thread'
    print str(e)

print 'Starting thread done'


while 1:
   pass