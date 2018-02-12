
d={'1':{'a':2, 'b':5}, 'c': 4}

ks = "1+b"

ks_new = 'd'
for item in ks.split('+'):
    ks_new = ks_new + '[' +str(`item`)+']'

print ks_new



print eval(ks_new)