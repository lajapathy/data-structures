#Implement iterator class to provide range functionality in reverse order


class reverseIter:
    def __init__(self,limit):
        self.limit=limit
        self.curr_value=limit-1

    def __iter__(self):
        return self

    def next(self):
        if self.curr_value>=0:
            temp=self.curr_value
            self.curr_value-=1
            return temp
        else:
            raise StopIteration

for i in reverseIter(5):
    print i
