#Implement an iterator class which returns consecutive  numbers

class yrange(object):
    def __init__(self,limit):
        self.i = 0
        self.limit = limit

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.limit:
            temp = self.i
            self.i += 1
            return temp


        raise StopIteration

x=yrange(5)
print(x)
import pdb;pdb.set_trace()
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())


def old_range(limit):
    list1 = []
    i=0
    while i<limit:
        list1.append(i)
        i+=1
    return list1


def zrange(limit):
    i=0
    import pdb;pdb.set_trace()
    while i<limit:
        temp = i
        i+=1
        yield temp


# m = yrange(5)
# x = zrange(5)

# for i in zrange(5):
#     import pdb;pdb.set_trace()
#     print (i)

