from leetcode.helper_modules.linked_list import LinkedList
from leetcode.helper_modules.node import Node

class LinkedListSum(object):

    def __init__(self):
        self.l3 = LinkedList()

    def add_two_nodes(self, n1, n2):
        return Node(n1.value + n2.value)

    def add_two_linked_list(self, l1, l2):
        l1_length = l1.get_length()
        l2_length = l2.get_length()

        if  l1_length > l2_length:
            while l1_length == l2_length:
                l2.add_node_at_tail(Node(0))

        if  l2_length > l1_length:
            while l1_length == l2_length:
                l1.add_node_at_tail(Node(0))

        while l1.head:
            self.l3.add_node_at_tail(Node(l1.get_tail_node().value + l2.get_tail_node().value))

            #Delete the tail_nodes
            l1.delete_tail_node()
            l2.delete_tail_node()

        return self.l3

