
#Implement a generator to implement xrange functionality

def my_generator(limit):
    print 'inside my_gen'
    i=0
    while i<limit:
        print 'about to yield '+str(i)
        yield i
        i+=1

print 'fff'
gen_obj = my_generator(4)
print type(gen_obj)
print gen_obj
#### NOTE : A generator function, when called only returns a generator object. It DOES NOT starts execution of the function.
### When we call next method, function executes till it hits "yield"
t = gen_obj.next()
print 'got '+str(t)

t = gen_obj.next()
print 'got '+str(t)

t = gen_obj.next()
print 'got '+str(t)

t = gen_obj.next()
print 'got '+str(t)

t = gen_obj.next()
print 'got '+str(t)

t = gen_obj.next()
print 'got '+str(t)



print 'gg'