#Find the first repeating character in a given string. Repeat the same for first non-repeating character

class Queue(object):
    def __init__(self):
        self.queue_list = []

    def enqueue(self, value):
        self.queue_list.insert(0, value)

    def dequeue(self):
        if self.queue_list:
            return self.queue_list.pop()
        return None

    def is_empty(self):
        return self.queue_list == []


class StringHelper(object):
    def __init__(self):
        self.char_dict = {}

    def get_first_repeating_char(self, str):
        for char in str:
            if char in self.char_dict.keys():
                return char
            self.char_dict[char] = 10
        return False

    def get_first_non_repeating_char(self, str):
        queue_obj = Queue()
        for char in str:
            if char in self.char_dict.keys():
                self.char_dict[char] = -1
            else:
                queue_obj.enqueue(char)
                self.char_dict[char] = 10

        #import pdb;pdb.set_trace()
        while not queue_obj.is_empty():
            queue_topmost = queue_obj.dequeue()
            if self.char_dict[queue_topmost] == 10:
                return queue_topmost
        return False

s=StringHelper()
print(s.get_first_repeating_char("lajju"))
s=StringHelper()
print(s.get_first_non_repeating_char("lajju"))

