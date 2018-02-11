
class Stack:
    def __init__(self):
        self.items=[]
        self.min = None

    def push(self,new_item):
        if not self.min:
            self.min=new_item
        else:
            self.min=min(self.min,new_item)
        self.items.append(new_item)

    def peek(self):
        try:
            return self.items[len(self.items)-1]
        except IndexError,e:
            return None
    def pop(self):
        return self.items.pop()
        #return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items==[]

    def print_stack(self):
        for i in self.items:
            print i

    def print_stack_reverse(self):
        for i in reversed(self.items):
            print i


    def get_min(self):
        return self.min