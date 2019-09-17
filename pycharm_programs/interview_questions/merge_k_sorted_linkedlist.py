
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self, node):
        self.head = node
    def add_node_at_end(self, data):
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = Node(data)

class Solution:
    def merge2SortedLinkedList(self, head1, head2):


