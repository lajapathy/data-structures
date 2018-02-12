#implement singly linked list with the following methods
# Insert: inserts a new node into the list
# Size: returns size of list
# Search: searches list for a node containing the requested data and returns that node if found, otherwise raises an error
# Delete: searches list for a node containing the requested data and removes it from list if found, otherwise raises an error

#5 -> 8 -> 10 ->
#5 is the head


class LinkedListNode(object):
    def __init__(self,value):
        self.value = value
        self.next = None

    def set_next(self,next_in):
        self.next = next_in

class singlyLinkedList(object):
    def __init__(self,head = None):
        self.head = head

    def insert(self,node_value):
        if not self.head:
            self.head = LinkedListNode(node_value)
        else:
            temp = LinkedListNode(node_value)
            temp.set_next(self.head)
            self.head = temp

    def size(self):
        count = 0
        x = self.head
        while x is not None:
            count+=1
            x=x.next

        return count

    def search(self,data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            else:
                current_node = current_node.next

        return None

    def delete(self,data):
        current_node = self.head
        found = false
        prev_node = None
        while not found:
            if current_node.data == data:
                found = True
            else:
                prev_node = current_node
                current_node = current_node.next
        if not prev_node:
            # This means we found the desired node at the head
            self.head = self.head.next
        else:
            prev_node.set_next(current_node.next)

    def append(self,data):
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next
            
        current_node.next = LinkedListNode(data)



a = LinkedListNode(5)
b = LinkedListNode(10)
print (a.value)
print (a.next)
print (b.value)
print (b.next)

a.set_next(b)