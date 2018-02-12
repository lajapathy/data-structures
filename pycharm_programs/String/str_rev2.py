
#String reverse using recursion

def str_rev(str1):
    if len(str1) == 1:
        return str1
    else:
        return str_rev(str1[1:]) + str1[0]

print str_rev('Kanakanak a town in Alaska')