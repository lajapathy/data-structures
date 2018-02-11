
# Pre order - Root left right
# in order - left root right
# post order - left right root


class Node(object):
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None

class Tree(object):
    def __init__(self,node):
        self.root=node

    def return_root(self):
        return self.root

    def add_left_child(self,left_child,node=None):
        if not node:
            node = self.root
        node.left_child = left_child
        return node.left_child

    def add_right_child(self,right_child,node=None):
        if not node:
            node = self.root
        node.right_child = right_child
        return node.right_child

    def print_tree_inorder(self,start_node):
        if not start_node:
            return None

        self.print_tree_inorder(start_node.left_child)
        print start_node.value
        self.print_tree_inorder(start_node.right_child)

    def print_tree_preorder(self,start_node):
        if not start_node:
            return None
        print start_node.value
        self.print_tree_preorder(start_node.left_child)
        self.print_tree_preorder(start_node.right_child)

    def print_tree_postorder(self,start_node):
        if not start_node:
            return None
        self.print_tree_postorder(start_node.left_child)
        self.print_tree_postorder(start_node.right_child)
        print start_node.value

    def get_max_width(self):
        pass


tree_obj = Tree(Node(1))
x = tree_obj.add_left_child(Node(2),tree_obj.root)
y = tree_obj.add_right_child(Node(3),tree_obj.root)
tree_obj.add_left_child(Node(4),x)
tree_obj.add_right_child(Node(5),x)
tree_obj.print_tree_preorder(tree_obj.root)
print '***'
tree_obj.print_tree_inorder(tree_obj.root)
print '***'
tree_obj.print_tree_postorder(tree_obj.root)
