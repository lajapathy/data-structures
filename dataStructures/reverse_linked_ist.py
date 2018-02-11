#Given a linked list, reverse the linked list and return it.
import pdb

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert_at_end(self, node_value):
        if not self.head:
            self.head = Node(node_value)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(node_value)

    def print_linked_list(self, current_node=None):
        if not current_node:
            current_node = self.head
        while(current_node.next):
            print(current_node.value)
            current_node = current_node.next
        print(current_node.value)


    def reverse_linked_list(self):
        ''' Reverses the linked list '''
        prev = None
        curr = self.head
        while(curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = next




r_obj = LinkedList()
r_obj.insert_at_end(5)
r_obj.insert_at_end(6)
r_obj.insert_at_end(7)
r_obj.insert_at_end(8)
r_obj.print_linked_list()
print("***")
r_obj.reverse_linked_list()
r_obj.print_linked_list()



