
class stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def printContents(self):
	 for item in self.items:
		print item
     def returnList(self):
	 return self.items

     def emptyContents(self):
	 del self.items[:]
