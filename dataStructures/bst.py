
from dataStructures.binary_search_tree import Node

class Bst(Node):

    def __init__(self, root_value=0):
        self.root = Node(root_value)

    def insert_element(self, value, parent=None):
