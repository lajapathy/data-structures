
def add1(val, i=0):
    i+=1
    val = val + i
    return val

sum1 = add1(10)
sum2 = add1(6,0)
sum3 = add1(5)

print ("sum1 = %s" % sum1)
print ("sum2 = %s" % sum2)
print ("sum3 = %s" % sum3)