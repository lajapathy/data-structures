
from singly_linked_list import LinkedListNode

class orderedLinkedList(object):
    def __init__(self,head = None):
        self.head = head

    def add(self,item):
        if not self.head:
            self.head = LinkedListNode(item)
            return

        if item < self.head.data:
            temp = self.head
            self.head = LinkedListNode(item)
            self.head.next = temp
            return

        # At this point, item is definitely greater than self.head.data
        prev_node = self.head
        current_node = self.head.next
        if not current_node:
            self.head.next = LinkedListNode(item)
            return
        while(current_node):
            if item < current_node :
                # we need to insert item between prev_node and curr_node
                temp = LinkedListNode(item)
                prev_node.next = temp
                temp.next = current_node
                break
            prev_node = current_node
            current_node = current_node.next




