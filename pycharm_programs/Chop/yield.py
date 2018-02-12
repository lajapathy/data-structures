

#Defining my own iterator class
class my_iterator:
    def __init__(self,limit):
        print 'inside init method'
        self.limit=limit
        self.curr_value=0

    def __iter__(self):
        print 'inside iter method'
        return self

    def next(self):
        print 'inside next'
        if self.curr_value<self.limit:
            temp=self.curr_value
            self.curr_value+=1
            return temp
        else:
            raise StopIteration

x = my_iterator(5)
print iter(x)
for i in iter(x):
    print i
