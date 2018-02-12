

def f(*args,**kwargs): print(args, kwargs)
def f2(arg1,arg2,*args,**kwargs): print(arg1,arg2, args, kwargs)

l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}

f2(1,2,3)
f2(*l,**d)
f2(*t,**d)
f2(7,8,a=1,b=2,c=3)
f2(1,2,*t,q="winning",**d)


#### NOTE : ** unpacks dictionary and * unpacks tuple