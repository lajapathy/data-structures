from leetcode.helper_modules.linked_list import LinkedList
from leetcode.helper_modules.node import Node
from leetcode.helper_modules.linked_list_sum import LinkedListSum

l1 = LinkedList()
l2 = LinkedList()

l1.add_node_at_tail(Node(3))
l1.add_node_at_tail(Node(2))
l1.add_node_at_tail(Node(5))

l2.add_node_at_tail(Node(1))
l2.add_node_at_tail(Node(4))
l2.add_node_at_tail(Node(2))

LinkedListSum().add_two_linked_list(l1, l2).print_linked_list()
