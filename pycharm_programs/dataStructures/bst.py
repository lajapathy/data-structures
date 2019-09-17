

class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left_child = None
        self.right_child = None


class Bst(object):
    def __init__(self, head):
        self.head = TreeNode(head)

    def insert(self, val, curr_node=None):
        if not curr_node:
            curr_node = self.head
        if val == curr_node.val:
            return True
        if val > curr_node.val:
            if not curr_node.right_child:
                curr_node.right_child = TreeNode(val)
                return True
            curr_node = self.head.right_child
            self.insert(val, curr_node)
        if val < curr_node.val:
            if not curr_node.left_child:
                curr_node.left_child = TreeNode(val)
                return True
            curr_node = self.head.left_child
            self.insert(val, curr_node)

    def preorder(self, curr_node=None):
        if not curr_node:
            return
        print curr_node
        self.preorder(curr_node.left_child)
        self.preorder(curr_node.right_child)

    def inorder(self, curr_node=None):
        if not curr_node:
            return
        self.preorder(curr_node.left_child)
        print curr_node
        self.preorder(curr_node.right_child)

    def preorder(self, curr_node=None):
        if not curr_node:
            return
        self.preorder(curr_node.left_child)
        self.preorder(curr_node.right_child)
        print curr_node