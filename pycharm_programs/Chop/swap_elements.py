#Swap two given elements in list


def swap_elements(a,x,y):
    x_index=a.index(x)
    y_index=a.index(y)
    a[x_index]=y
    a[y_index]=x
    return a


a=[3,4,5,6,7,8]
swap_elements(a,5,7)
print a
