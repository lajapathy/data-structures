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
t = gen_obj.next()
print 'got '+str(t)

t = gen_obj.next()
print 'got '+str(t)


for i in my_generator(5):
    print i

for i in xrange(5):
    if i==2:
        break