
import math

class TreeNode(object):
    def __init__(self, val):
        self.value = val
        self.lchild = None
        self.rchild = None

class Bst(object):
    def __init__(self, treeNode=None):
        self.root = treeNode

    def inorder_traverse(self, curr_node=None):
        if not curr_node:
            return
        self.inorder_traverse(self.curr_node.lchild)
        print self.curr_node.value
        self.inorder_traverse(self.curr_node.rchild)


def arr_to_bst(arr, root=None):
    if len(arr) == 1:
        return TreeNode(arr[0])
    if not root:
        root = TreeNode(arr[int(math.floor(len(arr)/2))])
    root.lchild = arr_to_bst(arr[:len(arr) /2], root)
    root.rchild = arr_to_bst(arr[len(arr) /2:], root)
    return root

import pdb;pdb.set_trace()
bst = Bst(arr_to_bst([1,4,5,6,7,8,9,]))
bst.inorder_traverse()