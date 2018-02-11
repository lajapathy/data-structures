#Given a binary tree, write a function to get the maximum width of the given tree.
# Width of a tree is maximum of widths of all levels.

from tree1 import Tree,Node

def find_max_width_recursion(start_node):
    pass
def get_width(start_node,level):
    pass

def find_max_width_iterative(start_node):
    if start_node is None:
        return 0
    q=[]
    max_width = 0
    q.insert(0,start_node)
    while (q != []):
        count = len(q)
        max_width = max(count,max_width)

        while count != 0:
            temp=q[0]
            q.pop()
            if temp.left_child:
                q.insert(0,temp.left_child)
            if temp.right_child:
                q.insert(0,temp.right_child)
    return max_width


tree_obj = Tree(Node(1))
x = tree_obj.add_left_child(Node(2),tree_obj.root)
y = tree_obj.add_right_child(Node(3),tree_obj.root)
tree_obj.add_left_child(Node(4),x)
tree_obj.add_right_child(Node(5),x)
tree_obj.add_left_child(Node(6),y)
tree_obj.add_right_child(Node(7),y)